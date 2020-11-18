
public class Produto {
    private String nome;
    private int codigo;
    private int qtdEstoque;
    private float precoUnitario;

    Produto(String nome, int codigo, int qtdEstoque, float precoUnitario) {
        this.nome = nome;
        this.codigo = codigo;
        this.qtdEstoque = qtdEstoque;
        this.precoUnitario = precoUnitario;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public void setCodigo(int codigo) {
        this.codigo = codigo;
    }

    public void setQtdEstoque(int qtdEstoque) {
        this.qtdEstoque = qtdEstoque;
    }

    public void setPrecoUnitario(float precoUnitario) {
        this.precoUnitario = precoUnitario;
    }

    public String getNome() {
        return this.nome;
    }

    public int getCodigo() {
        return this.codigo;
    }

    public float getPrecoUnitario() {
        return this.codigo;
    }

    public int getQtdEstoque() {
        return this.qtdEstoque;
    }
}
