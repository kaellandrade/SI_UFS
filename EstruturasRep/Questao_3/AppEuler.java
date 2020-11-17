import java.util.Scanner;

public class AppEuler {
    public static void main(String[] args) {
        int valor;

        Scanner sc = new Scanner(System.in);
        Euler eul = new Euler();

        System.out.println("Digite um número inteiro: ");
        valor = sc.nextInt();
        eul.setNumero(valor);

        System.out.printf("E = %.2f\n",  eul.calculaE());
        sc.close();
    }
}
