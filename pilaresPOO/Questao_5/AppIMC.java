import java.util.Scanner;

public class AppIMC {
    public static void main(String[] args) {
        PessoaIMC pessoas[] = new PessoaIMC[2];
        Scanner sc = new Scanner(System.in);
        int resposta;

        for (int i = 0; i < pessoas.length; i++) {
            System.out.println("[1] Mulher [2] Homem");
            resposta = sc.nextInt();
            System.out.println("Digite o nome, data nascimento, peso e altura respectivamente");
            if (resposta == 1) {
                PessoaIMC p_mulher = new Mulher(sc.next(), sc.next(), sc.nextDouble(), sc.nextDouble());
                pessoas[i] = p_mulher;
            } else {
                PessoaIMC p_homem = new Homem(sc.next(), sc.next(), sc.nextDouble(), sc.nextDouble());
                pessoas[i] = p_homem;

            }
        }

        imprimeObj(pessoas);
    }

    public static void imprimeObj(PessoaIMC pessoas[]) {
        for (int i = 0; i < pessoas.length; i++) {
            System.out.println(pessoas[i]);
            System.out.println(pessoas[i].resultIMC());
        }
    }
}
