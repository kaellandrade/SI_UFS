
public class Conjunto {
    int uni[] = new int[20];
    int dif[] = new int[10];
    int interc[] = new int[10];

    public int[] encontraUniao(int x[], int y[]) {
        int uniIndex = 0;
        for (int i = 0; i < x.length; i++) {
            if (!estaContido(x[i], uni)) {
                uni[uniIndex] = x[i];
                uniIndex++;
            }

            if (!estaContido(y[i], uni)) {
                uni[uniIndex] = y[i];
                uniIndex++;
            }
        }
        return uni;

    }

    public int[] encontraDif(int x[], int y[]) {
        int difIndex = 0;
        for (int i = 0; i < x.length; i++) {
            if (!estaContido(x[i], y) && !estaContido(x[i], dif)) {
                dif[difIndex] = x[i];
                difIndex++;
            }

        }
        return dif;
    }

    public int[] encontraInterc(int x[], int y[]) {
        int intercIndex = 0;
        for (int i = 0; i < x.length; i++) {
            if (estaContido(x[i], y) && !estaContido(x[i], interc)) {
                interc[intercIndex] = x[i];
                intercIndex++;
            }

        }
        return interc;
    }

    public static boolean estaContido(int x, int arr[]) {
        for (int i = 0; i < arr.length; i++) {
            if (x == arr[i])
                return true;
        }
        return false;
    }

}
