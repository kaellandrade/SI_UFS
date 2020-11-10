
public class Circulo {
    private float raio;
    private final float PI = 3.14f;

    public void setRaio(float valor ){
        raio = valor;
    }
    public float Area() {
        return PI * (raio * raio);
    }
}
