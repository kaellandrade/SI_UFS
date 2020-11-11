import java.util.Scanner;

public class AppCalcPeso {
    public static void main(String[] args) {
        float peso;
        final float GRAVIDA_TERRA = 9.807f;

        Scanner sc = new Scanner(System.in);
        Lua lua = new Lua();

        System.out.println("Digite seu peso na terra em KG");
        peso = sc.nextFloat();
        
        lua.setMassa(peso/GRAVIDA_TERRA);

        System.out.printf("Seu peso na lua será: %.2f KG\n", lua.calcPeso());
        sc.close();
        
    }
}