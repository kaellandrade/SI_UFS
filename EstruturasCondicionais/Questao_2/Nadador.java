import java.util.Set;

public class Nadador {
    private int idade;

    public void setIdade(int valor) {
        idade = valor;
    }

    public String mostraCategoria() {
        if (idade >= 0 && idade <= 10) {
            return "Infantil";

        } else if (idade >= 11 && idade <= 15) {
            return "Jovem";

        } else if (idade >= 16 && idade <= 30) {
            return "Adolescente";

        } else if (idade >= 31 && idade <= 45) {
            return "Adulto";
            
        } else {
            return "Sênior";
        }
    }
}
