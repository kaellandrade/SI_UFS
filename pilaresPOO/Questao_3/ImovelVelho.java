public class ImovelVelho extends Imovel{
    ImovelVelho(String endereco, float preco){
        super(endereco, preco);
    }

    @Override
    public float getPreco() {
        return super.getPreco();
    }

    public float taxaPreco() {
        return super.getPreco() - super.getPreco()*0.3f;
    }

    
    
}