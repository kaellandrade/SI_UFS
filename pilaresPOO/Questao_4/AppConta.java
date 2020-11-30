public class AppConta {
    public static void main(String[] args){
        Conta  contcorrente = new ContaCorrente(1000, 0.2f);
        Conta  contpoupanca = new ContaPoupanca(1000, 0.2f); 

        contcorrente.atualizar();
        contpoupanca.atualizar();

        System.out.print("Corrente: "); imprimeSaldo(contcorrente);
        System.out.print("Poupança: "); imprimeSaldo(contpoupanca);

        contcorrente.depositar(600);
        contpoupanca.depositar(400);

        System.out.print("Corrente: "); imprimeSaldo(contcorrente);
        System.out.print("Poupança: "); imprimeSaldo(contpoupanca);

        contcorrente.sacar(500);
        contpoupanca.sacar(500);

        


        System.out.print("Corrente: "); imprimeSaldo(contcorrente);
        System.out.print("Poupança: "); imprimeSaldo(contpoupanca);


        
    }

    public static void imprimeSaldo(Conta cont) {
        System.out.println("Saldo: " + cont.getSaldo());
    }
    
}
