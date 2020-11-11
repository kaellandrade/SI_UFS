import java.util.Scanner;

public class AppInverteNum {

    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        Inversor invert = new Inversor();

        int num1, num2, num3;

        System.out.println("Digite três valores inteiros: ");
        num1 = sc.nextInt();
        invert.setNumUm(num1);

        num2 = sc.nextInt();
        invert.setNumDois(num2);

        num3 = sc.nextInt();
        invert.setNumTres(num3);

        System.out.println("Os valores invertidos são: ");
        System.out.println(invert.inverteNumeros());

        sc.close();
        
    }

}