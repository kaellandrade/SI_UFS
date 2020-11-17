public class Banco {
    private final float PORCENTAGEM = 0.3f;
    private float salBruto;
    private float descontos;
    private float emprestimo;
    private float salarioLiquido;

    public void setDesconto(float desconto) {
        this.descontos = desconto;
    }

    public void setSalbruto(float salBruto) {
        this.salBruto = salBruto;
    }

    public void setEmprestimo(float emprestimo) {
        this.emprestimo = emprestimo;
    }

    public float calSalLiquid() {
        this.salarioLiquido = this.salBruto - this.descontos;
        return this.salarioLiquido;
    }

    public void concedeEmprestimo(){
        if(this.emprestimo <= this.salarioLiquido*PORCENTAGEM)
            System.out.println("Emprestimo CONCEDIDO");
        else
            System.out.println("Emprestimo NEGADO");
    }

}