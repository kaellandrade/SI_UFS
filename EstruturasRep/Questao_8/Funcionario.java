public class Funcionario {
    private final float SALARIOINICIAL = 1000f;
    private final int ANOCONTRATO = 2005;
    private final int FIMCONTRATO = 2016;
    private float novoSalario;

    public float calculaAumento(float percentual, float valor) {
        return (percentual * valor) + valor;
    }

    public void exibeExtrato() {
        float percAnoAnterior = 1.5f / 100f;

        for (int i = ANOCONTRATO; i <= FIMCONTRATO; i++) {
            if (i >= 2007)
                percAnoAnterior *= 2;

            this.novoSalario = calculaAumento(percAnoAnterior, SALARIOINICIAL);
            System.out.printf("ANO %d ----> R$ %.2f\n", i, this.novoSalario);
        }
    }
}