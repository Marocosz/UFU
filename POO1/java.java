// Aula 01 

import java.util.Scanner;

public class Soma {
    public static void main(String[] args){
        Scanner entrada = new Scanner(System.in);
        
        System.out.print("Digite o valor do primeiro número: ");
        int num1 = entrada.nextInt();
        
        System.out.print("Digite o valor do segundo número: ");
        int num2 = entrada.nextInt();
        
        int soma = num1 + num2;
        
        System.out.println("A soma dos dois números é: " + soma);
    }
}

