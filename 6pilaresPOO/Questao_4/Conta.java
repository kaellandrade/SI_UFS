public class Conta {
    protected float saldo;
    protected final float TAXA;

    Conta(float saldo, float TAXA){
        this.saldo = saldo;
        this.TAXA = TAXA;
    }
    public float getSaldo() {
        return this.saldo;
    }

    public void depositar(float valor) {
        this.saldo += valor;
    }

    public void atualizar(){
        this.saldo = (this.TAXA * this.saldo) + this.saldo;
    }

    public void sacar(float valor){
        if(this.saldo >= valor)
            this.saldo -= valor;
        else
            System.out.println("Valor indisponível");
    }
}
