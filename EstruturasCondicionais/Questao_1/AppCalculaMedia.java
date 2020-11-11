import java.util.Scanner;

public class AppCalculaMedia {
    public static void main(String[] args) {
        float valor;
        Aluno aluno = new Aluno();
        Scanner sc = new Scanner(System.in);

        System.out.println("1º Nota: ");
        valor = sc.nextFloat();
        aluno.setNota1(valor);

        System.out.println("2º Nota: ");
        valor = sc.nextFloat();
        aluno.setNota2(valor);

        System.out.println("3º Nota: ");
        valor = sc.nextFloat();
        aluno.setNota3(valor);

        System.out.printf("Média: %.2f\n", aluno.calcMedia());
        System.out.printf("Status: %s\n", aluno.verificaAprovacao());

        sc.close();
    }
}
