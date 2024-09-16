package com.mycompany.pooaulas;

import java.time.LocalDate;

public class PessoaFisica extends Cliente {

    private long cpf;
    private LocalDate dataNasc;

    public PessoaFisica(long cpf) {
        this.cpf = cpf;
    }

    public PessoaFisica(long cpf, LocalDate dataNasc, String nome, String endereco) {
        super(nome, endereco);
        this.cpf = cpf;
        this.dataNasc = dataNasc;
    }
    // equivalente a 
    /*public PessoaFisica(long cpf, LocalDate dataNasc, String nome, String endereco) {
        this.nome = nome;
        this.endereco = endereco;
        this.cpf = cpf;
        this.dataNasc = dataNasc;
    }*/
    

    @Override
    public void mostrar() {
        super.mostrar();
        System.out.println("Cpf: " + cpf);
    }

    public long getCpf() {
        return cpf;
    }

    public void setCpf(long cpf) {
        this.cpf = cpf;
    }

    public LocalDate getDataNasc() {
        return dataNasc;
    }

    public void setDataNasc(LocalDate dataNasc) {
        this.dataNasc = dataNasc;
    }

}
