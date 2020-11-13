public class Potencia {
    private final int BASE = 3;

    public void mostraPotencia() {
        int i = 0;
        while (i <= 9) {
            System.out.printf("%d ", calcPow(BASE, i));
            i++;
        }
        System.out.println();
    }

    public int calcPow(int base, int expoente) {
        int resultado = 1;
        if (expoente == 0)
            return 1;

        for (int i = 0; i < expoente; i++) {
            resultado *= base;
        }
        return resultado;
    }
}