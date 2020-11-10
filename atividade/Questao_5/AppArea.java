import java.util.Scanner;

public class AppArea {
    public static void main(String[] args) {
        float raio;

        Scanner scan = new Scanner(System.in);
        Circulo circulo = new Circulo();

        System.out.println("Entre com o valor do raio");
        raio = scan.nextFloat();

        circulo.setRaio(raio);
        
        System.out.printf("A área é: %.2f\n", circulo.Area());

    }
}
