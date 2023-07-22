package com.paymentMoMo.paymentMoMo.Resitory;

import com.paymentMoMo.paymentMoMo.model.PaymentModels;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.Optional;

public interface Repositorys extends JpaRepository<PaymentModels,Integer> {
    Optional<PaymentModels> findByPhones(Integer phones);

    PaymentModels findByPhones(String phones);

   

}
