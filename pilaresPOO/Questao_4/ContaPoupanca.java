public class ContaPoupanca extends Conta{

    ContaPoupanca(float saldo, float TAXA){
        super(saldo, TAXA);
    }

    @Override
    public void atualizar() {
        this.saldo = (this.TAXA*this.saldo*3) + this.saldo ;
    }
}
