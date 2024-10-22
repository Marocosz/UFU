package ordena;

class ContaCorrente implements Comparable<ContaCorrente> {
//class ContaCorrente {

    double saldo;
    String nome;

    public ContaCorrente() {
        this.saldo = 0.0;
    }

    public void deposita(double valor) {
        this.saldo += valor;
    }

    /**/
    public int compareTo(ContaCorrente outra) {
        if (this.saldo < outra.saldo) {
            return -1;
        } else if (this.saldo > outra.saldo) {
            return 1;
        } else {
            return 0; // saldos iguais
        }
    }
    /* */

}
