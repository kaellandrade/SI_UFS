public class Pessoa {
    String nome;
    String dataNascimento;

    Pessoa(String nome, String dataNascimento){
        this.nome = nome;
        this.dataNascimento = dataNascimento;
    }

    public String toString(){
        return "Nome: " + getNome() + 
            "\n" +"Data de Nascimento: "+getDataNascimento();
    }

    public String getNome(){
        return this.nome;
    }

    public String getDataNascimento(){
        return this.dataNascimento;
    }
}