
public class Tempo {
    private int hora;
    private int minutos;

    public void setHora(int valor) {
        hora = valor;
    }

    public void setMinutos(int valor) {
        minutos = valor;
    }

    public int getHora(){
        return hora;
    }

    public int getMinutos(){
        return minutos;
    }

    public int horaParaMinutos(){
        return hora * 60;
    }

    public int minutosParaSegundos(){
        return minutos * 60;
    }

    public int totalMinutos(){
        return horaParaMinutos() + getMinutos();
    }

    public int totalSegundos(){
        return totalMinutos() * 60;
    }
}
