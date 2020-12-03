public class Quadrado extends Figura{
    private float lado;

    Quadrado(float lado){
        this.lado = lado;
    }
    

    @Override
    public double calcularArea(){
        return lado*lado;
    } 
}
