
public class AppPrimo {
    public static void main(String[] args) {
        Numeros num = new Numeros();

        num.lerNumeros();
        System.out.printf("%s %20s\n", "Posição", "valor");
        num.imprimeNumeros();
        System.out.println();

    }
}
