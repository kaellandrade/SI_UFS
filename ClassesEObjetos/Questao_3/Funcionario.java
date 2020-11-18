public class Funcionario {
    private String nome;
    private char sexo;
    private String departamento;
    private float salario;

    Funcionario(String nome, char sexo, String departamento, float salario){
        this.nome = nome;
        this.sexo = sexo;
        this.departamento = departamento;
        this.salario = salario;

    }
    
    public void setDepartamento(String departamento) {
        this.departamento = departamento;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public void setSalario(float salario) {
        this.salario = salario;
    }

    public void setSexo(char sexo) {
        this.sexo = sexo;
    }

    public String getDepartamento() {
        return departamento;
    }

    public String getNome() {
        return nome;
    }

    public float getSalario() {
        return salario;
    }

    public char getSexo() {
        return sexo;
    }

    public void bonificar(float valor){
        this.salario += valor;
    }

    public float verGanhoAnual(){
        return salario * 13;
    }

}
