import java.util.Scanner;

public class AppConta {
    public static void main(String[] args) {
        float valor;
        Scanner sc = new Scanner(System.in);
        Conta conta = new Conta("Gandalf", 12345, 1000, 1000);

        System.out.printf("NOME: %s\nSALDO: R$ %.2f\n", conta.getNome(), conta.getSaldo());

        System.out.println("Quanto deseja depositar: ");
        valor = sc.nextFloat();
        conta.setDepositar(valor);

        System.out.println("Quanto deseja sacar: ");
        valor = sc.nextFloat();
        conta.sacar(valor);

        System.out.printf("NOME: %s\nSALDO: R$ %.2f\n", conta.getNome(), conta.getSaldo());

    }

}
