package com.mycompany.pooaulas;

public class UsandoHeranca {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Cliente cli = new Cliente();
        
        
        PessoaFisica f = new PessoaFisica(1234);
        f.setNome("Afonso Pena");
        f.mostrar();
        
            
    }
    
}
