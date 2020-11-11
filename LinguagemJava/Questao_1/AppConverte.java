import java.util.Scanner;

public class AppConverte{
    public static void main(String [] args){
        Galao galao = new Galao();
        Scanner sc = new Scanner(System.in);
        short totalGaloes;
        
        System.out.println("Digite a quantidade de galões");
        totalGaloes = sc.nextShort();
        galao.setQtdGaloes(totalGaloes);

        System.out.println(totalGaloes + " galões = " + 
                galao.converteGalaoLitros() + " L");
        sc.close();
    }
}
