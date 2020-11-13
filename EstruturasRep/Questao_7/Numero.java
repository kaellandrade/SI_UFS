
public class Numero {
    private int numero;

    public void setNumero(int numero){
        this.numero = numero;
    }

    public boolean ePrimo(){
        int divs = 0;
        if(numero <= 1 )
            return false;
        for(int i = 1; i <= this.numero; i++){
            if(this.numero % i == 0)
                divs++;
        }
        return (divs <= 2);
    }
}
