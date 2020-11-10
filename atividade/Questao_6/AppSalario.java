import java.util.Scanner;

public class AppSalario {

    public static void main (String [] args){
        float salMinimo;
        float salFuncionario;
        
        Scanner scan = new Scanner(System.in);
        Funcionario funcionario = new Funcionario();

        System.out.println("Digite o valor do salário mínimo atual ");
        salMinimo = scan.nextFloat();
        funcionario.setSalmin(salMinimo);

        System.out.println("Qual o seu salario? ");
        salFuncionario = scan.nextFloat();
        funcionario.setSalario(salFuncionario);

        System.out.printf("Você ganha %.1f salários(s) mínimo(s)\n",
                funcionario.contaSalario());

        
    }
    
}
