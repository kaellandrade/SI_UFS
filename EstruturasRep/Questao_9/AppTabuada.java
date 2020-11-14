import java.util.Scanner;

public class AppTabuada {
    public static void main(String[] args) {    
        int valor;
        Scanner sc = new Scanner(System.in);
        Tabuada tb = new Tabuada();

        valor = sc.nextInt();
        System.out.println("Digite uma valor inteiro");

        tb.setNumero(valor);
        tb.exibeTabuada();
        sc.close();
    }

}
