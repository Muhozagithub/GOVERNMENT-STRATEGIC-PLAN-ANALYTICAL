package com.paymentMoMo.paymentMoMo.services;

import com.paymentMoMo.paymentMoMo.model.HistoryTransaction;
import com.paymentMoMo.paymentMoMo.model.Parteners;
import com.paymentMoMo.paymentMoMo.model.PaymentModels;

import java.util.List;

public interface PaymentInterface {

    public Object MakePayment(String paymentPhone,double amount,int password,String transctionid);

    public String GreateUniqueTransId(int numberOfIdLenght);


    public Parteners createTransactionData(Parteners parteners);

    public PaymentModels createMoMoAccount(PaymentModels paymentModels);

    public List<HistoryTransaction> SumAllamount();

    public PaymentModels phoneAmount(String phone);

}
