import java.util.Scanner;

public class AppConsumoEnergia {
    public static void main(String[] args){
        double salario;
        double qtdKW;

        Scanner scan = new Scanner(System.in);
        ConsumoEnergia consumo = new ConsumoEnergia();
        
        System.out.println("Digite seu salário: ");
        salario = scan.nextDouble();
        
        System.out.println("Digite a quantidade de KW: ");
        qtdKW = scan.nextDouble();

        consumo.setSalario(salario);
        consumo.setKw(qtdKW);

        System.out.printf("Valor do KW: %.2f\n", consumo.calcularValorKw());
    

        System.out.printf("Valor a ser pago pela residência: %.2f\n", consumo.calcularValorResidencia());
        System.out.printf("Valor a ser pago com desconto: %.2f\n", consumo.aplicarDesconto());

    }
}
