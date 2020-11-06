import java.util.Scanner;

public class AppConsulta {
    public static void main(String[] args){
        String nome;
        float peso;
        float altura;
        char sexo;
        int idade;

        Scanner scan = new Scanner(System.in);
        Paciente paciente = new Paciente();

        System.out.println("Digite seu nome: ");
        nome = scan.nextLine();
        paciente.setNome(nome);

        System.out.println("Digite sua idade");
        idade = scan.nextInt();
        paciente.setIdade(idade);

        System.out.println("Digite seu peso: ");
        peso = scan.nextFloat();
        paciente.setPeso(peso);

        System.out.println("Digite sua altura: ");
        altura = scan.nextFloat();
        paciente.setAltura(altura);

        System.out.println("Digite seu sexo [F/M]:");
        sexo = scan.next().charAt(0);
        paciente.setSexto(sexo);

        System.out.println("****Ficha do paciente****");
        System.out.printf("Nome: %s\n", paciente.getNome());
        System.out.printf("Peso: %.2f\n", paciente.getPeso());
        System.out.printf("Altura: %.2f\n", paciente.getAltura());
        System.out.printf("Sexo: %c\n", paciente.getSexo());
        System.out.printf("Idade: %d\n", paciente.getIdade());
        System.out.printf("Preço da consulta: %.2f\n", paciente.calcularConsulta());


    }
}
