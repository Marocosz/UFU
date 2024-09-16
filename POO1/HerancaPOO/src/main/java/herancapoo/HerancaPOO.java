package herancapoo;

public class HerancaPOO {

    public static void main(String[] args) {
        Funcionario fs[] = new Funcionario[10];
        
        fs[0] = new Funcionario("Marcos", "14/12/2003", 1000.0);
        fs[1] = new Chefe("Ronaldo", "19/02/1992", 2000.0, 100.0);
        
        fs[0].mostrar();
        fs[1].mostrar();
    }
}
