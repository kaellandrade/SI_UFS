import java.util.Scanner;

public class AppConverte{
    public static void main(String [] args){
        Conversor conversor = new Conversor();
        Scanner qtGalao = new Scanner(System.in);
        short totalGaloes;
        
        System.out.println("Digite a quantidade de galões");
        totalGaloes = qtGalao.nextShort();
        conversor.setQtdGaloes(totalGaloes);

        System.out.println(totalGaloes + " galões corresponde a " + conversor.converteGalaoLitros() +" L");
    }
}