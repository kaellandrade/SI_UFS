import java.util.Scanner;

public class Numeros {
    private int numbers[] = new int[10];
    private int quantidadePares;
    private int quantidadeImpares;

    public void lerNumeros() {
        Scanner sc = new Scanner(System.in);
        for (int i = 0; i < numbers.length; i++) {
            System.out.print((i + 1) + "º: ");
            numbers[i] = sc.nextInt();
        }
        sc.close();
    }

    public void imprimePares() {
        for (int i = 0; i < numbers.length; i++) {
            if (numbers[i] % 2 == 0) {
                System.out.printf(" %d", numbers[i]);
                this.quantidadePares++;
            }
        }
    }

    public void imprimeImpares() {
        for (int i = 0; i < numbers.length; i++) {
            if (numbers[i] % 2 != 0) {
                System.out.printf(" %d", numbers[i]);
                this.quantidadeImpares++;
            }
        }
    }

    public int getTotalImpares() {
        return this.quantidadeImpares;
    }

    public int getTotalPares() {
        return this.quantidadePares;
    }
}