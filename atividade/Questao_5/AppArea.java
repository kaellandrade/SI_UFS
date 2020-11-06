import java.util.Scanner;

public class AppArea {
    public static void main(String[] args) {
        double raio;

        Scanner scan = new Scanner(System.in);
        Circulo circulo = new Circulo();

        System.out.println("Entre com o valor do raio");
        raio = scan.nextDouble();
        circulo.setRaio(raio);
        System.out.printf("A área é: %.2f\n", circulo.Area());

    }
}
