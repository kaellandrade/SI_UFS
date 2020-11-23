
public class Venda {
    public static void main(String[] args) {
        Produto p1, p2;
        Item item1, item2, item3;

        p1 = new Produto("Detergente", 1234, 4, 1.99f);
        p2 = new Produto("Sabonte", 0001, 60, 0.99f);

        item1 = new Item(p1.getCodigo(), p1, 1);
        item2 = new Item(p2.getCodigo(), p2, 1);
        item3 = new Item(p1.getCodigo(), p1, 1);

        System.out.printf("\n****Quantidade em estoque****\n");
        System.out.printf("%s ---- %d\n", p1.getNome(), p1.getQtdEstoque());
        System.out.printf("%s ---- %d\n", p2.getNome(), p2.getQtdEstoque());


        System.out.printf("\n****Vendas****\n");
        System.out.printf("Produto vendido: %s\n", item1.getProduto().getNome());
        System.out.printf("Quantidade vendida: %d\n", item1.getQtdVendas());
        System.out.printf("Preço unitário: R$: %.2f\n", item1.getProduto().getPrecoUnitario());
        System.out.printf("Pago na venda: R$: %.2f\n", item1.getProduto().getPrecoUnitario() * item1.getQtdVendas());

        item1.modificaQtdEstoque();
        item2.modificaQtdEstoque();
        item3.modificaQtdEstoque();
        
        System.out.printf("\nProduto vendido: %s\n", item2.getProduto().getNome());
        System.out.printf("Quantidade vendida: %d\n", item2.getQtdVendas());
        System.out.printf("Preço unitário: R$: %.2f\n", item2.getProduto().getPrecoUnitario());
        System.out.printf("Pago na venda: R$: %.2f\n", item2.getProduto().getPrecoUnitario() * item2.getQtdVendas());



        System.out.printf("\nProduto vendido: %s\n", item3.getProduto().getNome());
        System.out.printf("Quantidade vendida: %d\n", item3.getQtdVendas());
        System.out.printf("Preço unitário: R$: %.2f\n", item3.getProduto().getPrecoUnitario());
        System.out.printf("Pago na venda: R$: %.2f\n", item3.getProduto().getPrecoUnitario() * item3.getQtdVendas());


        System.out.printf("\n****Quantidade em estoque****\n");
        System.out.printf("%s ---- %d\n", p1.getNome(), p1.getQtdEstoque());
        System.out.printf("%s ---- %d\n", p2.getNome(), p2.getQtdEstoque());
        


    }

}
