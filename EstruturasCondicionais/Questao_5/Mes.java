
public class Mes {
    public String nome;

    public void setNome(String value) {
        nome = value;
    }

    public int calcNumMes() {
        
        switch (nome){
            case "Janeiro":
                return 1;
            case ("Fevereiro"):
                return 2;
            case ("Março"):
                return 3;
            case ("Abril"):
                return 4;
            case ("Maio"):
                return 5;
            case ("Junho"):
                return 6;
            case ("Julho"):
                return 7;
            case ("Agosto"):
                return 8;
            case ("Setembro"):
                return 9;
            case ("Outubro"):
                return 10;
            case ("Novembro"):
                return 11;
            case ("Dezembro"):
                return 12;
            default:
                return 0;

        }
    }

}
