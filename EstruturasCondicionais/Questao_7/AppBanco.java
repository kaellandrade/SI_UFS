import java.util.Scanner;

public class AppBanco {
    public static void main(String [] args){
        Scanner sc = new Scanner(System.in);
        Banco bc = new Banco();

        float valor;
        System.out.println("Digite o valor do salário bruto: ");
        valor = sc.nextFloat();
        bc.setSalbruto(valor);

        System.out.println("Digite o valor dos descontos: ");
        valor = sc.nextFloat();
        bc.setDesconto(valor);

        System.out.println("Digite o valor do empréstimo");
        valor = sc.nextFloat();
        bc.setEmprestimo(valor);

        bc.calSalLiquid();
        bc.concedeEmprestimo();
        sc.close();

    }

}
