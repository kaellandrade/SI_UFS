
public class ConsumoEnergia {
    private double salario;
    private double quantidadeKW;

    public void setSalario(double valor) {
        salario = valor;
    }

    public void setKw(double kw) {
        quantidadeKW = kw;
    }

    public double calcularValorKw() {
        return salario * 0.2;
    }

    public double calcularValorResidencia() {
        return calcularValorKw() * quantidadeKW;
    }

    public double aplicarDesconto() {
        return calcularValorResidencia() - (calcularValorResidencia() * 0.15);
    }
}
