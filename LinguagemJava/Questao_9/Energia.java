
public class Energia {
    private float salario;
    private float quantidadeKW;

    public void setSalario(float valor) {
        salario = valor;
    }

    public void setKw(float kw) {
        quantidadeKW = kw;
    }

    public float calcularValorKw() {
        return salario * 0.2f;
    }

    public float calcularValorResidencia() {
        return calcularValorKw() * quantidadeKW;
    }

    public float aplicaDesconto() {
        return calcularValorResidencia() - (calcularValorResidencia() * 0.15f);
    }
}
