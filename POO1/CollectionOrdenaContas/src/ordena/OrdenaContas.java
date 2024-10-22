package ordena;

import java.util.List;
import java.util.ArrayList;
import java.util.Collections; // método sort()

public class OrdenaContas {

    public static void main(String[] args) {
        ContaCorrente c1 = new ContaCorrente();
        c1.deposita(500);
        ContaCorrente c2 = new ContaCorrente();
        c2.deposita(200);
        ContaCorrente c3 = new ContaCorrente();
        c3.deposita(150);

        List<ContaCorrente> contas = new ArrayList<>();
        contas.add(c1);
        contas.add(c2);
        contas.add(c3);

        for (ContaCorrente s : contas) {
            System.out.println(s.saldo);
        }
        System.out.println("================");
        Collections.sort(contas); // qual seria o critério para esta ordenação?
        for (ContaCorrente s : contas) {
            System.out.println(s.saldo);
        }
    }

}
