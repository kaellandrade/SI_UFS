public class Conta {
    private final float SALARIOMIN = 940f;
    private String nome;
    private int numeroConta;
    private float saldo;
    private float limiteSaque;

    Conta(String nome, int numeroConta, float saldo, float limite) {
        this.nome = nome;
        this.numeroConta = numeroConta;
        this.saldo = saldo;
        this.limiteSaque = (limite > SALARIOMIN) ? SALARIOMIN : limite;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public float getSaldo() {
        return this.saldo;
    }

    public float getLimite() {
        return this.limiteSaque;
    }
    public String getNome(){
        return this.nome;
    }

    public boolean sacar(float valor) {
        
        if (valor <= this.saldo && valor <= this.limiteSaque){
            this.saldo -= valor;
            return true;
        }else{
            return false;
        }
    }

    public void setDepositar(float valor) {
        this.saldo += valor;
    }

}
