public class Tabuada {
    private final int INICIO = 1;
    private final int FIM = 10;
    private int numero;

    public void setNumero(int numero) {
        this.numero = numero;
    }

    public void exibeTabuada(){
        for(int i = INICIO; i <= FIM; i++){
            System.out.printf("%d + %2d = %d \n", this.numero, i, this.numero + i);
        }
    }
}