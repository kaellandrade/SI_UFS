
public class Galao {
    private short qtdGaloes;
    private final float LITRO_UM_GALAO = 3.7854f;

    public void setQtdGaloes(short quantidadeGaloes) {
        qtdGaloes = quantidadeGaloes;
    }

    public float converteGalaoLitros() {
        return qtdGaloes * LITRO_UM_GALAO;
    }

}
