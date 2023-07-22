package com.paymentMoMo.paymentMoMo.model;

import jakarta.persistence.*;
import lombok.Data;

@Data
@Entity
public class PaymentModels {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private int id;
    @Column(unique=true)
    private int phones;
    private int password;
    private double amount;
}
