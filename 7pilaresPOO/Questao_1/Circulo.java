
public class Circulo extends Figura{
    private double raio;

    Circulo(double raio){
        this.raio = raio;
    }
    
    @Override
    public double calcularArea(){
        return Math.PI * Math.pow(this.raio, 2);
    } 

}
