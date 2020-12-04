public class Vendedor extends Empregado{
    private int cotaVendas;
    Vendedor(String nome, int idade, String telefone, float salario, int contaVendas){
        super(nome, idade, telefone, salario);
        super.setSalario(salario);
        this.cotaVendas = contaVendas;
    }
    
    public void vender(){
        if(this.cotaVendas > 0)
            --this.cotaVendas;
    }

    public String toString(){
        return String.format("-------\nVendedor: %s\nIdade: %d\nTelefone: %s\nSalário: %.2f\nCota Vendas: %d", 
        super.getNome(), super.getIdade(), super.getTelefone(), super.getSalario(), cotaVendas);
    }
}
