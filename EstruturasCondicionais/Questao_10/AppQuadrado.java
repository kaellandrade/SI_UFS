import java.util.Scanner;

public class AppQuadrado {
    public static void main(String[] args) {
        double valor;
        Scanner sc = new Scanner(System.in);
        Quadrado qd1 = new Quadrado();
        Quadrado qd2 = new Quadrado();
        Quadrado qd3 = new Quadrado();

        System.out.println("Digite os lados para o 1º Quadrado, 2º quadrado e 3º quadrado, respectivamente");
        valor = sc.nextDouble();
        qd1.setLado(valor);

        valor = sc.nextDouble();
        qd2.setLado(valor);

        valor = sc.nextDouble();
        qd3.setLado(valor);

        System.out.println(calcMaiorArea(qd1, qd2, qd3));
        System.out.println(calcMenorPerimetro(qd1, qd2, qd3));
        sc.close();
    }

    public static String calcMaiorArea(Quadrado q1, Quadrado q2, Quadrado q3) {
        double area1;
        double area2;
        double area3;
        area1 = q1.calcularArea();
        area2 = q2.calcularArea();
        area3 = q3.calcularArea();
        if (area1 >= area2 && area2 >= area3) {
            return "1º quadrado sua área: " + area1;
        } else if (area2 >= area1 && area1 >= area3) {
            return "2º quadrado sua área: " + area2;
        } else {
            return "3º quadrado sua área: " + area3;
        }
    }

    public static String calcMenorPerimetro(Quadrado q1, Quadrado q2, Quadrado q3) {
        double p1;
        double p2;
        double p3;
        p1 = q1.CalcularPerimetro();
        p2 = q2.CalcularPerimetro();
        p3 = q3.CalcularPerimetro();
        if (p1 <= p2 && p2 <= p3) {
            return "1º quadrado perímetro: " + p1;
        } else if (p2 <= p1 && p1 <= p3) {
            return "2º quadrado perímetro: " + p2;
        } else {
            return "3º quadrado perímetro: " + p3;
        }
    }

}
