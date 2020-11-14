
import java.util.Scanner;

public class Jogador {
    private final int QTDJOGADORES = 5;
    private String nome;
    private int idade;
    private float peso;
    private int QtdMenorIdade;
    private int QtdSomaIdade;
    private int QtdAcima18Quilos;

    Scanner sc = new Scanner(System.in);

    public void lerJogadores() {
        int i = 1;
        do {
            System.out.printf("%dº Jogador: Digite o nome, idade e peso, respectivamente: \n", i);
            this.nome = sc.next();
            this.idade = sc.nextInt();
            this.peso = sc.nextFloat();

            this.QtdSomaIdade += idade; // Soma todas idades
            if (idade < 18) // Conta jogadores com idade < 18
                this.QtdMenorIdade++;
            if(peso > 80)
                QtdAcima18Quilos++;
            i++;
        } while (i <= QTDJOGADORES);
        sc.close();
    }

    public float calcPercentagem() {
        return (this.QtdAcima18Quilos * 100) / QTDJOGADORES;
    }

    public float mediaIdade() {
        return this.QtdSomaIdade / QTDJOGADORES;
    }

    public void imprimeHistorico(){
        
       System.out.printf("Quantidade de jogadores menores de idade: %d\n", this.QtdMenorIdade);
       System.out.printf("Média das idades: %.2f\n", this.mediaIdade()); 
       System.out.printf("Percentagem de jogadores com mais de 80KG: %.2f%%\n", this.calcPercentagem()); 
    }

}
