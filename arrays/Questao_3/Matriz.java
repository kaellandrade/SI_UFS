import java.util.Scanner;

public class Matriz {
    public int maior;
    private int linha;
    private int coluna;

    Matriz(int LINHA, int COLUNA) {
        this.linha = LINHA;
        this.coluna = COLUNA;
    }

    public void preencheMatriz(int m[][], int r[][]) {
        Scanner sc = new Scanner(System.in);
        for (int i = 0; i < linha; i++) {
            for (int j = 0; j < coluna; j++) {
                System.out.printf("%dº Linha %dº Coluna", (i + 1), (j + 1));
                m[i][j] = sc.nextInt();
                r[i][j] = m[i][j];
            }
        }
    }

    public void imprimeMatriz(int mat[][]) {
        int i = 0;
        int j = 0;
        while (i < linha) {
            j = 0;
            while (j < coluna) {
                System.out.printf("|%d|", mat[i][j]);
                j++;
            }
            i++;
            System.out.println();
        }
    }

    public int encontrarMaior(int mat[][]) {
        this.maior = mat[0][0];
        for (int i = 0; i < linha; i++) {
            for (int j = 0; j < coluna; j++) {
                if (mat[i][j] > this.maior)
                    this.maior = mat[i][j];
            }
        }
        return this.maior;
    }

    public void multiplicarMatriz(int mat[][], int x) {
        for (int i = 0; i < linha; i++) {
            for (int j = 0; j < coluna; j++)
                mat[i][j] = mat[i][j] * x;
        }
    }

}