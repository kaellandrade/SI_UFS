import java.util.Scanner;

public class AppMedia {
    public static void main(String[] args) {
        int valor;

        Scanner sc = new Scanner(System.in);
        Media media = new Media();

        System.out.println("Digite o 1º nota ");
        valor = sc.nextInt();
        media.setNum1(valor);

        System.out.println("Digite o 2º nota ");
        valor = sc.nextInt();
        media.setNum2(valor);

        System.out.println("Digite o 3º nota ");
        valor = sc.nextInt();
        media.setNum3(valor);

        System.out.print("Sua média: ");
        System.out.println(media.calcMedia());

        sc.close();
    }
}
