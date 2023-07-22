package com.paymentMoMo.paymentMoMo.Resitory;

import com.paymentMoMo.paymentMoMo.model.Parteners;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.Optional;

public interface Transaction extends JpaRepository<Parteners,Integer> {
    Parteners findByTransactionid(String transactionid);


}
