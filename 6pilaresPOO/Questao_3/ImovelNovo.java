public class ImovelNovo extends Imovel{
    ImovelNovo(String endereco, float preco){
        super(endereco, preco);
    }

    @Override
    public float getPreco() {
        return super.getPreco();
    }

    public float taxaPreco(){
        return super.getPreco() + super.getPreco()*0.1f;
    }


    
}
