import java.util.Scanner;

public class AppConsumoEnergia {
    public static void main(String[] args){
        float salario;
        float qtdKW;

        Scanner sc = new Scanner(System.in);
        Energia consumo = new Energia();
        
        System.out.println("Digite seu salário: ");
        salario = sc.nextFloat();
        
        System.out.println("Digite a quantidade de KW: ");
        qtdKW = sc.nextFloat();

        consumo.setSalario(salario);
        consumo.setKw(qtdKW);

        System.out.printf("Valor do KW: R$ %.2f\n", consumo.calcularValorKw());
    

        System.out.printf("Valor a ser pago pela residência: R$ %.2f\n", 
                consumo.calcularValorResidencia());

        System.out.printf("Valor a ser pago com desconto: R$ %.2f\n", 
                consumo.aplicaDesconto());

        sc.close();
    }
}
