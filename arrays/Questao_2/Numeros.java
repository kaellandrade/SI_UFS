import java.util.Scanner;

public class Numeros {
    private int valores[] = new int[3];
    private int maior;
    private int menor;

    public void lerValores() {
        int i = 0;
        Scanner sc = new Scanner(System.in);

        while (i < valores.length) {
            System.out.print((i + 1) + "º: ");
            valores[i] = sc.nextInt();
            i++;
        }
    }

    public int getMenor() {
        return this.menor;
    }

    public int getMaior() {
        return this.maior;
    }

    public void encontrarMaiorMenor() {
        this.maior = valores[0];
        this.menor = valores[0];
        for (int i = 1; i < this.valores.length; i++) {
            if (valores[i] > this.maior)
                this.maior = valores[i];

            if (valores[i] < this.menor)
                this.menor = valores[i];
        }
    }

}
