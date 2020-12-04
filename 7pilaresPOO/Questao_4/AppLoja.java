public class AppLoja {
    public static void main(String[] args){
        final float SALMIN = 1100f;
        Pessoa cliente; 
        Vendedor vendedor; 
        Gerente gerente;

        cliente = new Cliente("Paulo", 25, "(75)9999-111", true);
        vendedor = new Vendedor("José", 19, "(79)9999-222", SALMIN, 5);
        gerente = new Gerente("Maria", 45, "(75)9999-333", SALMIN, "RH");

        System.out.println(cliente);
        System.out.println(vendedor);
        System.out.println(gerente);

        vendedor.vender();


        System.out.println(vendedor);

    }
    
}