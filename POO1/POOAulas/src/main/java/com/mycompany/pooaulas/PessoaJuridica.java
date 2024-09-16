package com.mycompany.pooaulas;

import java.time.LocalDate;

public class PessoaJuridica extends Cliente {

    private long cnpj;
    private LocalDate dataInscricaoCnpj;

    public long getCnpj() {
        return cnpj;
    }

    public void setCnpj(long cnpj) {
        this.cnpj = cnpj;
    }

    public LocalDate getDataInscricaoCnpj() {
        return dataInscricaoCnpj;
    }

    public void setDataInscricaoCnpj(LocalDate dataInscricaoCnpj) {
        this.dataInscricaoCnpj = dataInscricaoCnpj;
    }

}
