import java.util.Scanner;

public class Palindromo {
    public static void main(String[] args) {
        
        char nome[] = new char[10];
        String entrada;

        System.out.println("Digite um nome");

        Scanner sc = new Scanner(System.in);
        entrada = sc.next();
        nome = entrada.toCharArray();
        
        System.out.println((isPalindromo(nome, inverteArray(nome))?"Palindromo":"Não é palídromo"));

    }

    public static char[] inverteArray(char arr[]) {
        char nomeInvertido[] = new char[arr.length];
        int i = 0;
        int f = (arr.length - 1);
        while (f >= 0) {
            nomeInvertido[i] = arr[f];
            i++;
            f--;
        }
        return nomeInvertido;
    }

    public static boolean isPalindromo(char normal[], char invertido[]){
        for(int i = 0; i < normal.length; i++){
            if(normal[i] != invertido[i]){
                return false;
            }
        }
        return true;
    }
}