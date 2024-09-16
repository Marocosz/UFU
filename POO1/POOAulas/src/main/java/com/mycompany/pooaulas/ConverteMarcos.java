package com.mycompany.pooaulas;

import com.mycompany.pooaulas.TemperaturaMarcos;

public class ConverteMarcos {
    public static void main(String[] args) {
        TemperaturaMarcos temp = new TemperaturaMarcos(30.0);
        
        temp.CfF();
        temp.exibirF();
        
        temp.FfC();
        temp.exibirC();
         
    }
    
}
