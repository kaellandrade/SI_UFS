public class InverteNumeros {
    private int num1;
    private int num2;
    private int num3;

    public void setNumUm(int valor) {
        num1 = valor;
    }

    public void setNumDois(int valor) {
        num2 = valor;
    }

    public void setNumTres(int valor) {
        num3 = valor;
    }

    public String inverteNumeros(){
        return num3 + ", " + num2 + ", " + num1;
    }
}