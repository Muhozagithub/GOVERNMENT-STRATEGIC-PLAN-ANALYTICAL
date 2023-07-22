package com.paymentMoMo.paymentMoMo.model;

import jakarta.persistence.*;
import lombok.Data;

@Data
@Entity
public class Parteners {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private int id;
    @Column(unique=true)
    private String transactionid;
    @Column(unique=true)
    private String partnername;
}
