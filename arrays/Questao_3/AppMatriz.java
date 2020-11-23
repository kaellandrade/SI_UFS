
public class AppMatriz {
    public static void main(String[] args) {
        final int LINHA = 4;
        final int COLUNA = 4;

        int m[][] = new int[LINHA][COLUNA];
        int r[][] = new int[LINHA][COLUNA];

        Matriz mat = new Matriz(LINHA, COLUNA);

        mat.preencheMatriz(m, r);
        System.out.println("Matriz M: ");
        mat.imprimeMatriz(m);
        System.out.printf("Maior elemento de M: %d\n", mat.encontrarMaior(m));

        System.out.println("Matriz R: ");
        mat.multiplicarMatriz(r, mat.encontrarMaior(m));
        mat.imprimeMatriz(r);

    }
}
