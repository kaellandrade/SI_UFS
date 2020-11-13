
public class Numero {
    private final int INICIO = 0;
    private final int FIM = 100;

    public void mostrarParFor() {
        for (int i = INICIO; i <= FIM; i++) {
            if (ePar(i))
                System.out.printf("%d ", i);

        }
        System.out.println();

    }

    public void mostrarParWhile() {
        int i = INICIO;
        while (i <= FIM) {
            if (ePar(i))
                System.out.printf("%d ", i);
            i++;
        }
        System.out.println();
    }

    public void mostrarParDoWhile() {
        int i = INICIO;
        do {
            if (ePar(i))
                System.out.printf("%d ", i);
            i++;
        } while (i<=FIM);
        System.out.println();
    }

    public static boolean ePar(int x) {
        return (x % 2 == 0) ? true : false;
    }

}