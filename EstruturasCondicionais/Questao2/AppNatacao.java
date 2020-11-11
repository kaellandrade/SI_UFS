import java.util.Scanner;

public class AppNatacao {
    public static void main(String[] args) {
        int idade;

        Nadador nadador = new Nadador();
        Scanner sc = new Scanner(System.in);

        System.out.println("Digite sua idade: ");
        idade = sc.nextInt();
        nadador.setIdade(idade);

        System.out.printf("Você é um nadador %s\n", nadador.mostraCategoria());

        sc.close();

    }
}
