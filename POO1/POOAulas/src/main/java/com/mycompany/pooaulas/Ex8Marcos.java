package com.mycompany.pooaulas;

import java.util.Scanner;

public class Ex8Marcos {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Digite o tamanho da base do retângulo: ");
        double base = scanner.nextDouble();
        
        System.out.print("Digite o tamanho da altura do retângulo: ");
        double altura = scanner.nextDouble();
        
        double area = base * altura;
        
        System.out.println("Calculo da Área de um retângulo");
        System.out.println(area);
    }
    
}
