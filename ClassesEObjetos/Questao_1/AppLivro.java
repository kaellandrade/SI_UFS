public class AppLivro {
    public static void main(String[] args) {

        Livro livro1, livro2, livro3;

        livro1 = new Livro("Hobbit", 123, 7);
        livro2 = new Livro("Sherlock", 456, 4);
        livro3 = new Livro("Algoritmos", 444, 2);

        imprimeLivroObj(livro1, livro2, livro3);
        livro1.setQtdExemples(3);
        livro2.setQtdExemples(30);
        livro3.setQtdExemples(1);
        imprimeLivroObj(livro1, livro2, livro3);

    }

    public static void imprimeLivroObj(Livro livro1, Livro livro2, Livro livro3) {
        System.out.println("\nNúmero de exemplares");
        System.out.printf("%s ----- TOTAL: %d\n", livro1.getNome(), livro1.getQtdExemplares());
        System.out.printf("%s ----- TOTAL: %d\n", livro2.getNome(), livro2.getQtdExemplares());
        System.out.printf("%s ----- TOTAL: %d\n", livro3.getNome(), livro3.getQtdExemplares());
    }

}
