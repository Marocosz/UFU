package com.mycompany.pooaulas;

import java.time.LocalDate;

public class Cliente {
    protected String nome;
    protected String endereco;
    protected LocalDate dataCadastro;
    
    public Cliente () {};
    
    public Cliente(String nome, String endereco) {
        this.nome = nome;
        this.endereco = endereco;
    }
    
    
     
    
    public void mostrar() {
        System.out.println("Nome do Cliente: " + nome);
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getEndereco() {
        return endereco;
    }

    public void setEndereco(String endereco) {
        this.endereco = endereco;
    }

    public LocalDate getDataCadastro() {
        return dataCadastro;
    }

    public void setDataCadastro(LocalDate dataCadastro) {
        this.dataCadastro = dataCadastro;
    }
    
    
    
}
