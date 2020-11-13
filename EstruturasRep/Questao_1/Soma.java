
public class Soma {
    private int inicio;
    private int fim;
    private int soma;

    public void setInicio(int inicio) {
        this.inicio = inicio;
    }

    public void setFim(int fim) {
        this.fim = fim;
    }

    public int somarComFor() {
        this.soma = 0;
        for (int i = inicio; i <= fim; i++) {
            this.soma += i;
        }
        return this.soma;
    }

    public int somarComWhile() {
        this.soma = 0;
        int i = this.inicio;

        while (i <= fim) {
            soma += i;
            i++;
        }
        return this.soma;
    }

    public int somarComDoWhile() {
        this.soma = 0;
        int i = this.inicio;
        do {
            soma += i;
            i++;
        } while (i <= this.fim);

        return this.soma;
    }

}
