import java.util.Scanner;

public class AppPrimo {
    public static void main(String[] args){
        int valor;
        Scanner sc = new Scanner(System.in);
        Numero num = new Numero();
        
        valor = sc.nextInt();

        num.setNumero(valor);
        System.out.printf("%s\n", num.ePrimo() ? "Primo":"Não é primo");

        sc.close();
    }
}
