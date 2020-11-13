import java.util.Scanner;

public class AppTempo {

    public static void main(String[] args) {
        int valor;

        Scanner sc = new Scanner(System.in);
        Tempo tmp1 = new Tempo();
        Tempo tmp2 = new Tempo();

        System.out.println("Digita a hora, minutos e segundos do 1º obj");
        valor = sc.nextInt();
        tmp1.setHora(valor);

        valor = sc.nextInt();
        tmp1.setMinutos(valor);

        valor = sc.nextInt();
        tmp1.setSegundos(valor);

        System.out.println("Digita a hora, minutos e segundos do 2º obj");
        valor = sc.nextInt();
        tmp2.setHora(valor);

        valor = sc.nextInt();
        tmp2.setMinutos(valor);

        valor = sc.nextInt();
        tmp2.setSegundos(valor);
        System.out.println("Diferença de tempo em segundos: " + diferencaTempoObj(tmp1, tmp2));
    }

    public static int diferencaTempoObj(Tempo x, Tempo y) {
        if (x.calculaSegundos() >= y.calculaSegundos()) {
            return x.calculaSegundos() - y.calculaSegundos();
        } else {
            return y.calculaSegundos() - x.calculaSegundos();
        }
    }
}
