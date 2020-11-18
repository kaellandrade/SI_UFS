
public class AppFuncionario {
    public static void main(String[] args) {
        Funcionario fun = new Funcionario("Micael", 'M', "DCOMP", 4000f);


        System.out.printf("NOME: %s\nSalário: %.2f R$\nGanho Anual: %.2f\n", 
            fun.getNome(), fun.getSalario(), fun.verGanhoAnual());

        fun.bonificar(100f);

        System.out.printf("\nNOME: %s\nSalário: %.2f R$\nGanho Anual: %.2f\n", 
            fun.getNome(), fun.getSalario(), fun.verGanhoAnual());

    }
}
