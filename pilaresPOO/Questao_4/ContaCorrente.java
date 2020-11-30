public class ContaCorrente extends Conta{

    ContaCorrente(float saldo, float TAXA){
        super(saldo, TAXA);
    }

    @Override
    public void atualizar() {
        this.saldo = (this.TAXA*this.saldo*2) + this.saldo ;
    }


    @Override
    public void depositar(float valor) {
        this.saldo += valor - 0.1f;
    }    
    
}
