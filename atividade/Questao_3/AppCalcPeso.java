import java.util.Scanner;
public class AppCalcPeso {
    public static void main(String[] args) {
        float peso;
        // float massa;
        final double GRAVIDADETERRA = 9.807;
        Scanner valor = new Scanner(System.in);
        PesoLua peso_lua = new PesoLua();

        System.out.println("Digite seu peso na terra");
        peso = valor.nextFloat();
        
        peso_lua.setMassa(peso/GRAVIDADETERRA);

        System.out.printf("Seu peso na lua é: %.2f KG\n", peso_lua.calcPeso());

        
    }
}