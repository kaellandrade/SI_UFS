import java.util.Scanner;

public class AppSomaIntervalos {
    public static void main(String[] args){
        int valor;

        Scanner sc = new Scanner(System.in);
        Soma sum = new Soma();

        System.out.println("Digite um intervalo [x, y]");
        valor = sc.nextInt();
        sum.setInicio(valor);

        valor = sc.nextInt();
        sum.setFim(valor);

        System.out.printf("Soma com for: %d\n", sum.somarComFor());
        System.out.printf("Soma com while: %d\n", sum.somarComWhile());
        System.out.printf("Soma com do while: %d\n", sum.somarComDoWhile());


    }
}
