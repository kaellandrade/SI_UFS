import java.util.Scanner;

public class Numeros {
    int numeros[] = new int[10];
    
    public void lerNumeros(){
        Scanner sc = new Scanner(System.in);
        for(int i = 0; i < numeros.length; i++){
            numeros[i] = sc.nextInt();
        }
        sc.close();
    }

    public void imprimeNumeros(){
        for(int i = 0; i < numeros.length; i++){
            if(ePrimo(numeros[i])){
                System.out.printf("[%d] ----> %20d\n", i, numeros[i]);
            }
        }
    }
    
    
    
    public boolean ePrimo(int x) {
        int divisores = 0;
        if(x <= 1)
            return false;
        for (int i = 1; i <= x; i++) {
            if(x % i == 0)
                divisores++;
        }
        return divisores <= 2;
    }


}
