public class Funcionario {
    private float salarioatual;
    private float aumento;
    private final float PORCENTAGEM = 0.25f;

    public void setAumento(float salario) {
        aumento = salario * PORCENTAGEM;
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