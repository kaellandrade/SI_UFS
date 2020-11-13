
public class Quadrado {
    private double lado;

    public void setLado(double lado) {
        this.lado = lado;
    }

    public double getLado() {
        return this.lado;
    }

    public double calcularArea() {
        return lado * lado;
    }

    public double CalcularPerimetro() {
        return lado * 4;
    }
}
