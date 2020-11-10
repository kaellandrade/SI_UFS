import java.util.Scanner;

public class AppMedia {
    public static void main(String[] args) {
        int valor;

        Scanner scan = new Scanner(System.in);
        Media media = new Media();

        System.out.println("Digite o 1º valor ");
        valor = scan.nextInt();
        media.setNum1(valor);

        System.out.println("Digite o 2º valor ");
        valor = scan.nextInt();
        media.setNum2(valor);

        System.out.println("Digite o 3º valor ");
        valor = scan.nextInt();
        media.setNum3(valor);

        System.out.print("Sua média: ");
        System.out.println(media.calcMedia());

    }
}
