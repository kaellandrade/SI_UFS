
public class Matriz {
    private int linha;
    private int coluna;

    Matriz(int LINHA, int COLUNA) {
        this.linha = LINHA;
        this.coluna = COLUNA;
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

    public boolean buscaValor(int x, int mat[][]) {
        for (int i = 0; i < linha; i++) {
            for (int j = 0; j < coluna; j++) {
                if (mat[i][j] == x){
                    System.out.printf("%d, está em [%d] linha [%d] coluna\n", x, (i+1), (j+1));
                    return true;
                }
            }
        }
        System.out.println("valor não encontrado!");
        return false;
    }

    

}