import java.util.Scanner;

public class AppMes {

    public static void main(String[] args) {
        String mesNome;

        Scanner sc = new Scanner(System.in);
        Mes mes = new Mes();

        System.out.println("Escreva o nome de um mês: Ex: Abril");
        mesNome = sc.nextLine();
        mes.setNome(mesNome);

        System.out.printf("%d\n", mes.calcNumMes());
        
        sc.close();

    }

}
