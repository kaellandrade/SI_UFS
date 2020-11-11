import java.util.Scanner;

public class AppConsulta {
    public static void main(String[] args){
        String nome;
        float peso;
        float altura;
        char sexo;
        int idade;

        Scanner sc = new Scanner(System.in);
        Paciente paciente = new Paciente();

        System.out.println("Digite seu nome: ");
        nome = sc.nextLine();
        paciente.setNome(nome);

        System.out.println("Digite sua idade");
        idade = sc.nextInt();
        paciente.setIdade(idade);

        System.out.println("Digite seu peso: ");
        peso = sc.nextFloat();
        paciente.setPeso(peso);

        System.out.println("Digite sua altura: ");
        altura = sc.nextFloat();
        paciente.setAltura(altura);

        System.out.println("Digite seu sexo [F/M]:");
        sexo = sc.next().charAt(0);
        paciente.setSexto(sexo);

        System.out.println("****Ficha do paciente****");
        System.out.printf("Nome: %s\n", paciente.getNome());
        System.out.printf("Peso: %.2f\n", paciente.getPeso());
        System.out.printf("Altura: %.2f\n", paciente.getAltura());
        System.out.printf("Sexo: %c\n", paciente.getSexo());
        System.out.printf("Idade: %d\n", paciente.getIdade());
        System.out.printf("Preço da consulta: R$ %.2f\n", paciente.calcularConsulta());

        sc.close();

    }
}
