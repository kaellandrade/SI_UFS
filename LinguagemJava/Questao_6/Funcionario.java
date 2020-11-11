public class Funcionario {
    private float salario;
    private float salMin;

    public float contaSalario(){
        return salario / salMin;
    }

    public void setSalario(float sal_funcionario){
        salario = sal_funcionario;
    }

    public void setSalmin( float sal_minimio){
        salMin = sal_minimio;
    }
    
}
