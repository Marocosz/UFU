package ordena;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class OrdenaStrings {

    public static void main(String[] args) {
        ArrayList<String> lista = new ArrayList<>();
        lista.add("verde");
        lista.add("azul");
        lista.add("preto");

        System.out.println(lista);
        Collections.sort(lista);
        System.out.println(lista);

    }

}
