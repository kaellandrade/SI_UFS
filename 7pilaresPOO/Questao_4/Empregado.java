public class Empregado extends Pessoa {
    private float salario;
    Empregado(String nome, int idade, String telefone, float salario){
        super(nome, idade, telefone);
        this.salario = salario;
    }

    public void setSalario(float salario) {
        this.salario = salario;
    }

    public float getSalario() {
        return this.salario;
    }

    public String toString(){
        return String.format("-------\nNome: %s\nIdade: %d\nTelefone: %s\nSalário: %.2f", 
        super.getNome(), super.getIdade(), super.getTelefone(), salario);
    }
}
