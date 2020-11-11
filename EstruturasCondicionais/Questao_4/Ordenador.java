public class Ordenador {
    private int num1;
    private int num2;
    private int num3;

    public void setNum1(int valor) {
        num1 = valor;
    }

    public void setNum2(int valor) {
        num2 = valor;
    }

    public void setNum3(int valor) {
        num3 = valor;
    }

    public String ordenaDecrescente() {
        if (num1 >= num2 && num2 >= num3) {
            return num1 + ", " + num2 + ", " + num3;

        } else if (num1 >= num3 && num3 >= num2) {
            return num1 + ", " + num3 + ", " + num2;

        } else if (num2 >= num1 && num1 >= num3) {
            return num2 + ", " + num1 + ", " + num3;

        } else if (num2 >= num3 && num3 >= num1) {
            return num2 + ", " + num3 + ", " + num1;

        } else if (num3 >= num1 && num1 >= num2) {
            return num3 + ", " + num1 + ", " + num2;

        } else {
            return num3 + ", " + num2 + ", " + num1;
        }
    }

    public String ordenaCrescente() {
        if (num1 <= num2 && num2 <= num3) {
            return num1 + ", " + num2 + ", " + num3;

        } else if (num1 <= num3 && num3 <= num2) {
            return num1 + ", " + num3 + ", " + num2;

        } else if (num2 <= num1 && num1 <= num3) {
            return num2 + ", " + num1 + ", " + num3;

        } else if (num2 <= num3 && num3 <= num1) {
            return num2 + ", " + num3 + ", " + num1;

        } else if (num3 <= num1 && num1 <= num2) {
            return num3 + ", " + num1 + ", " + num2;

        } else {
            return num3 + ", " + num2 + ", " + num1;
        }
    }

}
