import java.util.Scanner;

public class AppArea {
    public static void main(String[] args) {
        float raio;

        Scanner sc = new Scanner(System.in);
        Circulo circulo = new Circulo();

        System.out.println("Entre com o valor do raio");
        raio = sc.nextFloat();

        circulo.setRaio(raio);
        
        System.out.printf("Área: %.2f\n", circulo.Area());

        sc.close();
    }
}
