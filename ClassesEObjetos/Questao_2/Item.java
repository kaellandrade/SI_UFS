
public class Item {
    private int codigo;
    private Produto produto;
    private int qtdVendas;

    Item(int codigo, /*Produto produto,*/ int qtdVendas) {
        this.codigo = codigo;
        // this.produto = produto;
        this.qtdVendas = qtdVendas;
    }

    public void setCodigo(int codigo) {
        this.codigo = codigo;
    }

    public void setProduto(Produto produto) {
        this.produto = produto;
    }

    public void setQtdVendas(int qtdVendas) {
        this.qtdVendas = qtdVendas;
    }

    public int getCodigo() {
        return this.codigo;
    }

    public Produto getProduto() {
        return this.produto;
    }

    public int getQtdVendas() {
        return this.qtdVendas;
    }

}
