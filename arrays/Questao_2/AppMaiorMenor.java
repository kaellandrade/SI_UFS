
public class AppMaiorMenor {
    public static void main(String[] args){
        Numeros nums = new Numeros();

        System.out.println("Digite dez valores: ");
        
        nums.lerValores();
        nums.encontrarMaiorMenor();

        System.out.printf("Maior valor lido: %d\nMenor valor lido: %d\n",
            nums.getMaior(), nums.getMenor());
    }
}
