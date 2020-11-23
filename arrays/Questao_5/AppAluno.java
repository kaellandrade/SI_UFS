import java.util.Scanner;

public class AppAluno {
    public static void main(String[] args) {
        Aluno alunos[] = new Aluno[3];
        Scanner sc = new Scanner(System.in);

        for (int i = 0; i < alunos.length; i++) {
            alunos[i] = new Aluno();
            System.out.print((i + 1) + "º Nome: ");
            alunos[i].setNome(sc.next());
            System.out.print("Nota de " + alunos[i].getNome() + ": ");
            alunos[i].setMedia(sc.nextFloat());
        }
        System.out.printf("%s obteve a maior nota.\n", maiorMedia(alunos));
        System.out.println("Alunos reprovados: ");
        mostraReprovados(alunos);
    }

    public static String maiorMedia(Aluno arr[]) {
        String nome = arr[0].getNome();
        float media = arr[0].getMedia();

        for (int i = 1; i < arr.length; i++) {
            if (arr[i].getMedia() > media)
                nome = arr[i].getNome();
        }
        return nome;
    }

    public static void mostraReprovados(Aluno arr[]) {
        int i = 0;
        while (i < arr.length) {
            if (arr[i].getMedia() < 5)
                System.out.printf("%s\n", arr[i].getNome());
            i++;
        }
    }
}
