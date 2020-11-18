
public class Produto {
    private String nome;
    private float precoCusto;
    private float precoVenda;

    public void setNome(String nome) {
        this.nome = nome;
    }

    public void setPrecoCusto(float precoCusto) {
        this.precoCusto = precoCusto;
    }

    public void setPrecoVenda(float precoVenda) {
        if (precoVenda < getPrecoCusto()) {
            System.out.println("ATENÇÃO: Preço de venda está inferior ao preço do custo!");
        } else {
            this.precoVenda = precoVenda;
        }
    }

    public float getPrecoCusto() {
        return this.precoCusto;
    }

    public float getPrecoVenda() {
        return this.precoCusto;
    }

    public String getNome() {
        return this.nome;
    }

    public float calcularMargemLucro() {
        if (this.precoVenda >= this.precoCusto)
            return this.precoVenda - this.precoCusto;
        else
            return 0;
    }

    public float getMargemLucroPorcentagem() {
        if (this.precoVenda >= this.precoCusto)
            return calcularMargemLucro() / getPrecoCusto() * 100f;
        else
            return 0;
    }

}
