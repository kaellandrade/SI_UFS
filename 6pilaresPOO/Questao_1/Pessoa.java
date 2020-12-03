public class Pessoa {
    private String nome;
    private String data;

    Pessoa(){
        this.nome = "";
        this.data = "";
    }

    Pessoa(String nome, String data){
        this.nome = nome;
        this.data = data;
    }

    public void setNome(String nome){
        this.nome = nome;
    }

    public void setData(String data){
        this.data = data;
    }

    public String getNome(){
        return this.nome;
    }

    public String getData(){
        return this.data;
    }
}
