import java.util.Scanner;

public class Numeros {
    private final int QTDNUMEROS = 10;
    private float numero;
    private float maior;
    private float soma;
    private float media;
    
    Scanner sc = new Scanner(System.in);

    public void lerNumeros(){
        float valor;
        int i = 1; 
        do{
            valor = sc.nextFloat();

            if(valor > 0){
                if(valor > this.maior)
                    this.maior = valor; // armazena o maior valor
                
                soma += valor; // Armazena a soma
                i++; // Incrementa apenas se o valor for positivo
            }
            else{
                System.out.println("Digite um número positivo!");
            }
        }while(i <= QTDNUMEROS);

        System.out.printf("Maior: %.2f\nSoma: %.2f\nMédia: %.2f\n",
            this.maior, this.soma, this.soma / QTDNUMEROS);

        sc.close();
    }

}
