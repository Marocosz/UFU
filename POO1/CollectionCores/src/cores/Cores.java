package cores;

import java.util.ArrayList;

public class Cores {

    public static void criarCores() {
        ArrayList<String> cores = new ArrayList<>();
        cores.add("Vermelho");
        cores.add("Verde");
        cores.add("Azul");
        cores.add("Amarelo");
        for (int i = 0; i < cores.size(); i++) {
            String str = cores.get(i);
            System.out.println(str);
        }
        cores.remove(3);
        cores.remove("Azul");

        System.out.println("=================");
        for (String s : cores) {
            System.out.println(s);
        }
        int indice = cores.indexOf("Vermelho");
        cores.set(indice, "Preto");
        System.out.println("=======================");
        for (String s : cores) {
            System.out.println(s);
        }
        cores.clear();
    } //Fim do método criarCores()

    public static void main(String args[]) {
        criarCores();
    }
}
