public class Funcionario {
    private float salarioatual;
    private float aumento;

    public void setAumento(float salario) {
        aumento = salario * 0.25f;
    }

    public void setSalario(float valor) {
        salarioatual = valor;
    }


    public float getNovoSalario() {
        return salarioatual + aumento;
    }

    public float getAumento() {
        return aumento;
    }

    public float getSalarioAtual(){
        return salarioatual;
    }
}