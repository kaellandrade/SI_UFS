import java.util.Scanner;

public class AppArea {
    public static void main(String[] args){
        int resposta;
        Figura fig;

        Scanner sc = new Scanner(System.in);
        System.out.println("[1] Quadrado\n[2] Triângulo\n[3]Círculo");
        
        resposta = sc.nextInt();
        if(resposta == 1)
            fig = new Quadrado(2);
        else if(resposta == 2)
            fig = new Triangulo(5, 7, 8);
        else
            fig = new Circulo(2);

        System.out.println(fig.calcularArea());
        sc.close();
    }    
}
