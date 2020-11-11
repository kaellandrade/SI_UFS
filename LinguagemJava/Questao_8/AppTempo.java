import java.util.Scanner;

public class AppTempo {
    public static void main(String[] args){
        int hora;
        int minutos;

        Scanner sc = new Scanner(System.in);
        Tempo temp = new Tempo();

        System.out.println("Digite a hora: ");
        hora = sc.nextInt();
        temp.setHora(hora);

        System.out.println("Digite os minutos: ");
        minutos = sc.nextInt();
        temp.setMinutos(minutos);

        System.out.printf("%d H quivale a %d M\n", temp.getHora(),
                temp.horaParaMinutos());
        System.out.printf("Total de minutos: %d\n", temp.totalMinutos());
        System.out.printf("Total de segundos: %d\n", temp.totalSegundos());

        sc.close();
    }
}
