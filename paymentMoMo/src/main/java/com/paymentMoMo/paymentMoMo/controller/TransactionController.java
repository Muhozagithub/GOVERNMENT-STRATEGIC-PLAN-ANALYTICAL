package com.paymentMoMo.paymentMoMo.controller;


import com.paymentMoMo.paymentMoMo.model.HistoryTransaction;
import com.paymentMoMo.paymentMoMo.model.Parteners;
import com.paymentMoMo.paymentMoMo.model.PaymentModels;
import com.paymentMoMo.paymentMoMo.services.PaymentInterface;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/transaction")
public class TransactionController {

    @Autowired
    private PaymentInterface paymentInterface;

    @PostMapping("/createMoMoAccount/")
    public PaymentModels createAccountMoMo(@RequestBody PaymentModels paymentModels){
        return paymentInterface.createMoMoAccount(paymentModels);
    }


    @PostMapping("/createTransaction/")
    public Parteners createTransactionDetails(@RequestBody Parteners parteners){
        int entrydata = 20;
        parteners.setTransactionid(paymentInterface.GreateUniqueTransId(entrydata));
        return paymentInterface.createTransactionData(parteners);
    }

    @GetMapping("/phoneamount/{phones}")
    public PaymentModels ShowAMount(@PathVariable String phones){
        return paymentInterface.phoneAmount(phones);
    }


    @PostMapping("/uriTrandaction/{phone}/{amount}/{passoword}/{transactionto}")
    public  Object createPayement(@PathVariable("phone") String phone, @PathVariable("amount") double amount, @PathVariable("passoword") Integer passoword,@PathVariable("transactionto") String transactionto){
        return  paymentInterface.MakePayment(phone,amount,passoword,transactionto);
    }

    @GetMapping("/amount/")
    public List<HistoryTransaction> Amount() {
        return paymentInterface.SumAllamount();
    }
}
