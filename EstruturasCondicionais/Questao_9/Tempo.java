public class Tempo {
    private int hora;
    private int minutos;
    private int segundos;

    public void setHora(int hora) {
        this.hora = hora;
    }

    public void setMinutos(int minutos) {
        this.minutos = hora;
    }

    public void setSegundos(int segundos) {
        this.segundos = segundos;
    }

    public int getHora() {
        return this.hora;
    }

    public int getMinutos() {
        return this.minutos;
    }

    public int getSegundos() {
        return this.segundos;
    }

    public int calculaSegundos(){
        return (this.hora * 3600) + (this.minutos * 60) + this.segundos;
    }
}
