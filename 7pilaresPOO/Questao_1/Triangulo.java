public class Triangulo extends Figura{
    private float lado1;
    private float lado2;
    private float lado3;

    Triangulo(float lado1, float lado2, float lado3){
        this.lado1 = lado1;
        this.lado2 = lado2;
        this.lado3 = lado3;
    }


    @Override
    public double calcularArea(){
        double p;
        p = (this.lado1 + this.lado2 + this.lado3) / 2;
        return Math.sqrt(p*(p-this.lado1)*(p-this.lado2)*(p-this.lado3));
    } 
    
}
