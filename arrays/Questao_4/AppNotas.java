import java.util.Scanner;

public class AppNotas {
    public static void main(String[] args) {
        final int TOTAL = 3;
        Scanner sc = new Scanner(System.in);
        String nomes[] = new String[TOTAL];
        float medias[] = new float[TOTAL];

        for (int i = 0; i < TOTAL; i++) {
            System.out.printf("%dº Nome: ", (i + 1));
            nomes[i] = sc.next();
            System.out.printf("Nota de %s: ", nomes[i]);
            medias[i] = sc.nextFloat();
        }

        System.out.printf("Aluno com maior média %s\n", alunoMaiorMedia(nomes, medias));
        System.out.println("Alunos reprovados: ");
        calcReprovados(nomes, medias);
        
    }

    public static String alunoMaiorMedia(String nomes[], float medias[]) {
        String nome = nomes[0];
        float media = medias[0];

        for (int i = 1; i < nomes.length; i++) {
            if (medias[i] > media) {
                nome = nomes[i];
            }
        }
        return nome;
    }

    public static void calcReprovados(String nomes[], float medias[]){
        for (int i = 1; i < nomes.length; i++) {
            if(medias[i] < 5){
                System.out.printf("%s\n", nomes[i]);
            }
        }
    }

}