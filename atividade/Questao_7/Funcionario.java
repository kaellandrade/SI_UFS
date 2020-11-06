public class Funcionario {
    private double salarioatual;
    private double aumento;

    public void setAumento(double salario) {
        aumento = salario * 0.25;
    }

    public void setSalario(double valor) {
        salarioatual = valor;
    }


    public double getNovoSalario() {
        return salarioatual + aumento;
    }

    public double getAumento() {
        return aumento;
    }

    public double getSalarioAtual(){
        return salarioatual;
    }
}