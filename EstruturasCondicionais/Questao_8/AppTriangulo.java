import java.util.Scanner;

public class AppTriangulo {
    public static void main(String[] args){
        float valor;
        Scanner sc = new Scanner(System.in);
        Triangulo triangulo = new Triangulo();
    
        System.out.println("Digite o valor do lado X");
        valor = sc.nextFloat();
        triangulo.setLadoX(valor);

        System.out.println("Digite o valor do lado Y");
        valor = sc.nextFloat();
        triangulo.setLadoY(valor);

        System.out.println("Digite o valor do lado Z");
        valor = sc.nextFloat();
        triangulo.setLadoZ(valor);

        System.out.println(triangulo.mostraTipo());

    }


}
