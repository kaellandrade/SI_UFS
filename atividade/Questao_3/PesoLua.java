public class PesoLua {
    private double massa;
    private final double GRAVIDADE = 1.66;

    public double calcPeso(){
        return massa * GRAVIDADE;
    }

    public void setMassa(double valor){
        massa = valor;
    }


}
