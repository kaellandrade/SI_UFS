
public class AppParImpar {
    public static void main(String[] args) {
        Numeros num = new Numeros();

        System.out.println("Digite 10 números");
        num.lerNumeros();
        System.out.println("Números pares lidos: ");
        num.imprimePares();
        System.out.println("\nNúmeros ímpares lidos: ");
        num.imprimeImpares();

        System.out.printf("\nQuantidade impares: %d\n Quantidade pares: %d\n", num.getTotalImpares(),
                num.getTotalPares());
    }
}
