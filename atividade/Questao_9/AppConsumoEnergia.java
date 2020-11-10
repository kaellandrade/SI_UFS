import java.util.Scanner;

public class AppConsumoEnergia {
    public static void main(String[] args){
        float salario;
        float qtdKW;

        Scanner scan = new Scanner(System.in);
        ConsumoEnergia consumo = new ConsumoEnergia();
        
        System.out.println("Digite seu salário: ");
        salario = scan.nextFloat();
        
        System.out.println("Digite a quantidade de KW: ");
        qtdKW = scan.nextFloat();

        consumo.setSalario(salario);
        consumo.setKw(qtdKW);

        System.out.printf("Valor do KW: R$ %.2f\n", consumo.calcularValorKw());
    

        System.out.printf("Valor a ser pago pela residência: R$ %.2f\n", 
                consumo.calcularValorResidencia());

        System.out.printf("Valor a ser pago com desconto: R$ %.2f\n", 
                consumo.aplicaDesconto());

    }
}
