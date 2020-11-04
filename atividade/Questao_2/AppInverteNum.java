import java.util.Scanner;
public class AppInverteNum{

    public static void main(String[] args){
        Scanner valor = new Scanner(System.in);
        InverteNumeros invert = new InverteNumeros();

        int num1;
        int num2;
        int num3;
        System.out.println("Digite três valores inteiros: ");
        num1 = valor.nextInt();
        invert.setNumUm(num1);

        num2 = valor.nextInt();
        invert.setNumDois(num2);

        num3 = valor.nextInt();
        invert.setNumTres(num3);

        System.out.println("Os valores invertidos são: ");
        System.out.println(invert.inverteNumeros());
    }
    
}