import java.util.Scanner;

public class AppOrdena {
    public static void main(String [] args){
        int valor;

        Scanner sc = new Scanner(System.in);
        Ordenador ordenador = new Ordenador();

        System.out.println("Digite três valores: ");

        valor = sc.nextInt();
        ordenador.setNum1(valor);

        valor = sc.nextInt();
        ordenador.setNum2(valor);

        valor = sc.nextInt();
        ordenador.setNum3(valor);

        System.out.printf("Crescente: %s\n", ordenador.ordenaCrescente());
        System.out.printf("Decrescente: %s\n", ordenador.ordenaDecrescente());

        sc.close();
    }
}
