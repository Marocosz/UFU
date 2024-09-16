
package herancapoo;

public class Funcionario {
    protected String nome, dataNascimento;
    protected double salario;

    // requisito para Herança
    public Funcionario(String nome, String dataNascimento, double salario) {
        this.nome = nome;
        this.dataNascimento = dataNascimento;
        this.salario = salario;
    }
    
    public void mostrar() {
        System.out.println("Nome: " + this.nome + " nasceu em: " + this.dataNascimento + ".");
    }
    

}
