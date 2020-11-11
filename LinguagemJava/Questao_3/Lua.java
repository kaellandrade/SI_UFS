public class Lua {
    private float massa;
    private final float GRAVIDADE = 1.66f;

    public float calcPeso(){
        return massa * GRAVIDADE;
    }

    public void setMassa(float valor){
        massa = valor;
    }


}
