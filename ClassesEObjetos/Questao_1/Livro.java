public class Livro {

    private int codigo;
    private String nome;
    private int qtdExemplares;

    Livro(String nome, int codigo, int qtdExemplares) {
        this.nome = nome;
        this.codigo = codigo;
        this.qtdExemplares = (qtdExemplares > 0 ? qtdExemplares : 0);
    }

    public void setCodigo(int codigo) {
        this.codigo = codigo;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public void setQtdExemples(int qtdExemplares) {
        this.qtdExemplares = (qtdExemplares > 0 ? qtdExemplares : 0);
    }

    public String getNome() {
        return this.nome;
    }

    public int getCodigo() {
        return this.codigo;
    }

    public int getQtdExemplares() {
        return this.qtdExemplares;
    }
}