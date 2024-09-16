package herancapoo;

public class Chefe extends Funcionario {
    private double adicional;

    public Chefe(String nome, String dataNascimento, double salario, double adicional) {
        super(nome, dataNascimento, salario);
        this.adicional = adicional;
    }
    
    @Override
    public void mostrar() {
        super.mostrar();
        System.out.println("Além disso ganha um adicional de: " + this.adicional);
    }
    
    
}
