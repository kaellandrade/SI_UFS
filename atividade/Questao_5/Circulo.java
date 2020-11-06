
public class Circulo {
    private double raio;
    private final double PI = 3.14;

    public void setRaio(double valor ){
        raio = valor;
    }
    public double Area() {
        return PI * (raio * raio);
    }
}
