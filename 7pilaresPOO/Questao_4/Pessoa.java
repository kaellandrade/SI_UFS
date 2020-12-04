public class Pessoa {
    private String nome;
    private int idade;
    private String telefone;

    Pessoa( String nome, int idade, String telefone){
        this.nome = nome;
        this.idade = idade;
        this.telefone = telefone;

    }
    
    public String getNome() {
        return nome;
    }

    public int getIdade() {
        return idade;
    }

    public String getTelefone() {
        return telefone;
    }

    public String toString(){
        return String.format("-------\nNome: %s\nIdade: %d\nTelefone: %s", 
        nome, idade, telefone);
    }
}
