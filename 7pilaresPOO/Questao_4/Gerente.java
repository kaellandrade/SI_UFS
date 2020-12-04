public class Gerente extends Empregado {
    private String setor;
    Gerente(String nome, int idade, String telefone, float salario, String setor){
        super(nome, idade, telefone, salario);
        super.setSalario(2*salario);
        this.setor = setor;
    }

    public String toString(){
        return String.format("-------\nGerente: %s\nIdade: %d\nTelefone: %s\nSalário: %.2f\nSetor: %s", 
        super.getNome(), super.getIdade(), super.getTelefone(), super.getSalario(), setor);
    }

}
