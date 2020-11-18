
public class Venda {
    public static void main(String[] args) {
        Produto p1, p2;
        Item item1, item2, item3;

        p1 = new Produto("Detergente", 1234, 4, 1.99f);
        p2 = new Produto("Sabonte", 0001, 60, 0.99f);

        item1 = new Item(1200, p1, 1);
        item2 = new Item(1300, p2, 2);
        item3 = new Item(1400, p1, 20);

        System.out.println("Quantidade em estoque");
        System.out.printf("%s ---- %d\n", p1.getNome(), p1.getQtdEstoque());
        System.out.printf("%s ---- %d\n", p2.getNome(), p2.getQtdEstoque());

        System.out.println("Quantidade em estoque");
        System.out.printf("%s ---- %d\n", p1.getNome(), p1.getQtdEstoque());
        System.out.printf("%s ---- %d\n", p2.getNome(), p2.getQtdEstoque());

    }

}
