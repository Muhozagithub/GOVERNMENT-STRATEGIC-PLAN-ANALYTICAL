package com.paymentMoMo.paymentMoMo.Resitory;

import com.paymentMoMo.paymentMoMo.model.HistoryTransaction;
import org.springframework.data.jpa.repository.JpaRepository;

public interface TransactionHistory extends JpaRepository<HistoryTransaction,Integer> {
}
