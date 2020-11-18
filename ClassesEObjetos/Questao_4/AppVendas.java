import java.util.Scanner;

public class AppVendas {

    public static void main(String[] args) {
        Produto prod1, prod2, prod3;
        // String nomeProduto;

        // float valorCusto;
        // float valorVenda;

        Scanner sc = new Scanner(System.in);

        prod1 = new Produto();
        prod2 = new Produto();
        prod3 = new Produto();

        System.out.printf("1º Nome produto: ");
        prod1.setNome(sc.next());

        System.out.printf("1º Preço de custo: ");
        prod1.setPrecoCusto(sc.nextFloat());

        System.out.printf("1º Preço de venda: ");
        prod1.setPrecoVenda(sc.nextFloat());

        System.out.printf("2º Nome produto: ");
        prod2.setNome(sc.next());
        System.out.printf("2º Preço de custo: ");
        prod2.setPrecoCusto(sc.nextFloat());
        System.out.printf("2º Preço de venda: ");
        prod2.setPrecoVenda(sc.nextFloat());

        System.out.printf("3º Nome produto: ");
        prod3.setNome(sc.next());
        System.out.printf("3º Preço de custo: ");
        prod3.setPrecoCusto(sc.nextFloat());
        System.out.printf("3º Preço de venda: ");
        prod3.setPrecoVenda(sc.nextFloat());

        System.out.printf("\n\nMargem Lucro: R$ %.2f\nMarge lucro: %.2f%%\n", prod1.calcularMargemLucro(),
                prod1.getMargemLucroPorcentagem());
        System.out.printf("Margem Lucro: R$ %.2f\nMarge lucro: %.2f%%\n", prod2.calcularMargemLucro(),
                prod2.getMargemLucroPorcentagem());
        System.out.printf("Margem Lucro: R$ %.2f\nMarge lucro: %.2f%%\n", prod3.calcularMargemLucro(),
                prod3.getMargemLucroPorcentagem());

    }

}
