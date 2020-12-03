public class AppAluno {
    public static void main(String[] args){
        Aluno aluno = new Aluno("Mika", "08/04/2000", 5.7f, 5.9f, 5.2f);
        System.out.printf( "Nome: %s\nData: %s\nMédia: %.2f\n", aluno.getNome(), aluno.getData(),
        (aluno.getNota1() + aluno.getNota2() + aluno.getNota3())/3);
    }
}
