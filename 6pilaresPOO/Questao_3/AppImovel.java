import java.util.Scanner;

public class AppImovel {
    public static void main(String[] args){
        int resposta;
        Scanner sc = new Scanner(System.in);
        
        System.out.printf("Digite 1 para novo 2 para velho: ");
        resposta = sc.nextInt();
        
        if(resposta == 1){
            ImovelNovo imovelnovo = new ImovelNovo("Rosa Elze", 100);
            System.out.println(imovelnovo.taxaPreco());
        }else{
            ImovelVelho imovelvelho = new ImovelVelho("Rosa Elze", 100);
            System.out.println(imovelvelho.taxaPreco());

        }

        
    }
}
