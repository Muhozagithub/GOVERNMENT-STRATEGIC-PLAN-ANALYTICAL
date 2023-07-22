package com.paymentMoMo.paymentMoMo.services;


import com.paymentMoMo.paymentMoMo.Resitory.Repositorys;
import com.paymentMoMo.paymentMoMo.Resitory.Transaction;
import com.paymentMoMo.paymentMoMo.Resitory.TransactionHistory;
import com.paymentMoMo.paymentMoMo.model.HistoryTransaction;
import com.paymentMoMo.paymentMoMo.model.Parteners;
import com.paymentMoMo.paymentMoMo.model.PaymentModels;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class ImpPayment  implements  PaymentInterface{

    @Autowired
    private Transaction transaction;

    @Autowired
    private TransactionHistory transactionHistory;
    @Autowired
    private Repositorys repositorys;


    @Override
    public Object MakePayment(String paymentPhone, double amount, int password,String transctionid) {
        Parteners transactionIDs=transaction.findByTransactionid(transctionid);
        if(transactionIDs!=null && transactionIDs.getTransactionid().equals(transctionid)){
            Optional<PaymentModels> findphondetail= Optional.ofNullable(repositorys.findByPhones(paymentPhone));
            if(findphondetail.isPresent()){
                PaymentModels payment=repositorys.findByPhones(paymentPhone);
                if(payment.getAmount() > amount && payment.getPassword()==password){
                    double amountDeduct=payment.getAmount() - amount;
                    payment.setAmount(amountDeduct);
                    repositorys.save(payment);
                    HistoryTransaction historyTransaction= new HistoryTransaction();
                    historyTransaction.setPhone(payment.getPhones());
                    historyTransaction.setAmount(amount);
                    historyTransaction.setPartnerid(transctionid);
                    historyTransaction.setPartnername(transactionIDs.getPartnername());
                    transactionHistory.save(historyTransaction);
                    return "SUCCESS";
                }else{
                    return "FAILED";
                }
            }else {
             return "Dear Customer, Phone number  "+paymentPhone+" is not in Mobile Money.";
            }
        }else {
         return "Unknown Transaction";
        }
    }


    public String GreateUniqueTransId(int numberOfIdLenght) {

        String COmbinatiooOfAllid = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" + "0123456789" + "abcdefghijklmnopqrstuvxyz";

        StringBuilder numberofStroed = new StringBuilder(numberOfIdLenght);

        for (int i = 0; i < numberOfIdLenght; i++) {

            int index = (int) (COmbinatiooOfAllid.length() * Math.random());
            numberofStroed.append(COmbinatiooOfAllid.charAt(index));
        }
        return numberofStroed.toString();
    }

    @Override
    public Parteners createTransactionData(Parteners parteners) {

        return transaction.save(parteners);
    }

    @Override
    public PaymentModels createMoMoAccount(PaymentModels paymentModels) {

        return repositorys.save(paymentModels);
    }

    @Override
    public List<HistoryTransaction> SumAllamount() {
        return transactionHistory.findAll();
    }

    @Override
    public PaymentModels phoneAmount(String parteners) {
        return repositorys.findByPhones(parteners);
    }


}
