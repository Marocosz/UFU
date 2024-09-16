package com.mycompany.pooaulas;

import java.util.Random;

public class Ex4Marcos {
    public static void main(String[] args) {
        Random random = new Random();
        int numLancamentos = 30000;
        int[] contagemSomas = new int[13];

        for (int i = 0; i < numLancamentos; i++) {
            int dado1 = random.nextInt(6) + 1; 
            int dado2 = random.nextInt(6) + 1; 
            int soma = dado1 + dado2; 
            contagemSomas[soma]++;
        }

        int maisFrequente = 2;
        int menosFrequente = 2;

        for (int i = 3; i <= 12; i++) {
            if (contagemSomas[i] > contagemSomas[maisFrequente]) {
                maisFrequente = i;
            }
            if (contagemSomas[i] < contagemSomas[menosFrequente]) {
                menosFrequente = i;
            }
        }

        for (int i = 2; i <= 12; i++) {
            System.out.println("Soma " + i + ": " + contagemSomas[i] + " ocorrências");
        }

        System.out.println("\nSoma mais frequente: " + maisFrequente + " com " + contagemSomas[maisFrequente] + " ocorrências.");
        System.out.println("Soma menos frequente: " + menosFrequente + " com " + contagemSomas[menosFrequente] + " ocorrências.");
    }
}
