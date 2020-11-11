import java.util.Scanner;

public class AppAumento {

    public static void main(String[] args){
        float salario;

        Scanner sc = new Scanner(System.in);
        Funcionario funcionario = new Funcionario();

        System.out.println("Digite seu salario atual");
        salario = sc.nextFloat();
        
        funcionario.setSalario(salario);
        funcionario.setAumento(salario); // Define o aumento para o salário atual

        System.out.printf("Seu salario é : R$ %.2f\n", funcionario.getSalarioAtual());
        System.out.printf("Aumento de R$ %.2f\n", funcionario.getAumento());
        System.out.printf("Seu novo salario é : R$ %.2f\n", funcionario.getNovoSalario());

        sc.close();

    }


}