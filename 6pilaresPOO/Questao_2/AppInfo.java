import java.util.Scanner;

public class AppInfo {
    public static void main(String[] args){
        int resposta;
        Integer i = new Integer(10);
        Scanner sc = new Scanner(System.in);
        Object [] data = {"Lista 5", new Object(), i};

        System.out.println("Digite 0, 1 ou 2");
        resposta = sc.nextInt();

        if(resposta >= 0 && resposta <= 2)
            System.out.println(data[resposta].getClass().getSimpleName());
        else
            System.out.println("Intervalo inválido!");
        

        
    }
}