public class Conversor {
    private short qtdGaloes;
    private final double LGALAO = 3.7854;

    public void setQtdGaloes(short quantidadeGaloes) {
        qtdGaloes = quantidadeGaloes;
    }

    public double converteGalaoLitros() {
        return qtdGaloes * LGALAO;
    }

}
