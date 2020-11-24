import java.util.Scanner;

public class AppConjunto {
    public static void main(String[] args) {
        Conjunto conj = new Conjunto();

        int x[] = new int[10];
        int y[] = new int[10];

        System.out.println("Digite 10 números para o vetor X");
        preencheArray(x);

        System.out.println("Digite 10 números para o vetor Y");
        preencheArray(y);
        
        System.out.println("\nX ∪ Y: ");
        imprimeArray(conj.encontraUniao(x, y));

        System.out.println("\nX - Y: ");
        imprimeArray(conj.encontraDif(x, y));

        System.out.println("\nX ∩ Y: ");
        imprimeArray(conj.encontraInterc(x, y));

    }

    public static void preencheArray(int arr[]) {
        Scanner sc = new Scanner(System.in);
        for (int i = 0; i < arr.length; i++) {
            arr[i] = sc.nextInt();
        }
    }

    public static void imprimeArray(int arr[]) {
        Scanner sc = new Scanner(System.in);
        for (int i = 0; i < arr.length; i++) {
            System.out.printf("%d ", arr[i]);
        }
        System.out.println();
    }

}
