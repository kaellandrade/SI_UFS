import java.util.Scanner;

public class AppAumento {

    public static void main(String[] args){
        float salario;
        Scanner scan = new Scanner(System.in);
        Funcionario funcionario = new Funcionario();

        System.out.println("Digite seu salario atual");
        salario = scan.nextFloat();
        
        funcionario.setSalario(salario);
        funcionario.setAumento(salario);

        System.out.printf("Seu salario é : %.2f\n", funcionario.getSalarioAtual());
        System.out.printf("Aumento de %.2f\n", funcionario.getAumento());
        System.out.printf("Seu novo salario é : %.2f\n", funcionario.getNovoSalario());



    }


}