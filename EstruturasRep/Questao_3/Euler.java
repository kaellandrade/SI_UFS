
public class Euler {
    private int numero;

    public void setNumero(int numero){
        this.numero = numero;
    }

    public double calculaE(){
        double e = 0;
        for (int i = 1; i <= numero; i++){
            e = e + (1.0/i);
        }
        return e;
    }

}
