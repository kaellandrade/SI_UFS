import java.util.Scanner;

public class AppSemana {
    public static void main(String[] args){
        int valor;

        Scanner sc = new Scanner(System.in);
        Semana semana = new Semana();

        valor = sc.nextInt();
        semana.setDia(valor);

        System.out.printf("%s\n", semana.mostrarDia());
    }




}
