import java.util.Scanner;


public class AppConsultaMatriz {
    public static void main(String[] args) {
        final int LINHA = 5;
        final int COLUNA = 8;
        boolean resposta;
        int valor;

        int matriz[][] = new int[LINHA][COLUNA];
        Matriz matr = new Matriz(LINHA, COLUNA);

        
        Scanner sc = new Scanner(System.in);
        preencheMatriz(matriz, LINHA, COLUNA);

        do{
            System.out.println("Digite o valor procurado: ");
            valor = sc.nextInt();
            matr.buscaValor(valor, matriz);
            resposta = imprimeMenu();

        }while(resposta);

    }

    public static void preencheMatriz(int m[][], int linha, int coluna) {
        Scanner teste = new Scanner(System.in);
        for (int i = 0; i < linha; i++) {
            for (int j = 0; j < coluna; j++) {
                System.out.printf("%dº Linha %dº Coluna: ", (i + 1), (j + 1));
                m[i][j] = teste.nextInt();
            }
        }
    }

    public static boolean imprimeMenu(){
        Scanner sc = new Scanner(System.in);
        System.out.print("Deseja fazer uma nova busca [false]/[true]: ");

        return sc.nextBoolean();
    }

}