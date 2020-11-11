import java.util.Scanner;

public class AppSalario {

    public static void main (String [] args){
        float salMinimo;
        float salFuncionario;
        
        Scanner sc = new Scanner(System.in);
        Funcionario funcionario = new Funcionario();

        System.out.println("Digite o valor do salário mínimo atual ");
        salMinimo = sc.nextFloat();
        funcionario.setSalmin(salMinimo);

        System.out.println("Qual o seu salário? ");
        salFuncionario = sc.nextFloat();
        funcionario.setSalario(salFuncionario);

        System.out.printf("Você ganha %.1f salários(s) mínimo\n",
                funcionario.contaSalario());

        sc.close();
        
    }
    
}
