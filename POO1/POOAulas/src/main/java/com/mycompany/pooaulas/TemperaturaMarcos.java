package com.mycompany.pooaulas;


public class TemperaturaMarcos {
    Double temperatura;
    
    public TemperaturaMarcos(Double temperatura) {
        this.temperatura = temperatura;
    }
    
    public void exibirC(){
        System.out.println("Temperatura: " + temperatura + "ºC");
    }
    
    public void exibirF() {
        System.out.println("Temperatura: " + temperatura + "ºF");
    }
    
    public void CfF() {
        temperatura = (temperatura * 9/5) + 32;
    }
    
    public void FfC(){
        temperatura = (temperatura - 32) * 5/9;
    }
}
