
public class Imovel {
    private String endereco;
    private float preco;

    Imovel(String endereco, float preco){
        this.endereco = endereco;
        this.preco = preco;
    }
    
    public void setEndereco(String endereco){
        this.endereco = endereco;
    }

    public void setPreco(float preco){
        this.preco = preco;
    }

    public String getEndereco(){
        return this.endereco;
    }

    public float getPreco(){
        return this.preco;
    }

    
}
