import java.util.Scanner;

public class AppCalculaMaior {
    public static void main(String[] args) {
        int valor;
        Scanner sc = new Scanner(System.in);
        CalculadorMaior cmaior = new CalculadorMaior();

        System.out.println("Digite 1º valor: ");
        valor = sc.nextInt();
        cmaior.setNum1(valor);

        System.out.println("Difite 2º valor: ");
        valor = sc.nextInt();
        cmaior.setNum2(valor);

        System.out.printf("Maior valor: %d\n", cmaior.cacularMaior());
        sc.close();
    }
}