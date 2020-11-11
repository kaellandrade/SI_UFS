
public class CalculadorMaior {
    private int num1;
    private int num2;

    public void setNum1(int valor) {
        num1 = valor;
    }

    public void setNum2(int valor){
        num2 = valor;
    }

    public int cacularMaior() {
        return (num1 > num2) ? num1 : num2;
    }

}
