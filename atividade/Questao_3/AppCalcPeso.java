import java.util.Scanner;
public class AppCalcPeso {
    public static void main(String[] args) {
        float peso;
        final float GRAVIDA_TERRA = 9.807f;

        Scanner valor = new Scanner(System.in);
        PesoLua peso_lua = new PesoLua();

        System.out.println("Digite seu peso na terra");
        peso = valor.nextFloat();
        
        peso_lua.setMassa(peso/GRAVIDA_TERRA);

        System.out.printf("Seu peso na lua será: %.2f KG\n", peso_lua.calcPeso());

        
    }
}