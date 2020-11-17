import java.util.Scanner;

public class AppNumeroPar {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Numero nump = new Numero();

        System.out.println("While:");
        nump.mostrarParWhile();

        System.out.println("For:");
        nump.mostrarParFor();

        System.out.println("Do While:");
        nump.mostrarParDoWhile();
        sc.close();

    }

}
