import java.util.Scanner;

public class Data {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int data1[] = new int[5];
        int data2[] = new int[4];
        int data3[] = new int[data1.length + data2.length];
        for (int i = 0; i < data1.length; i++) {
            data1[i] = sc.nextInt();
        }
        for (int i = 0; i < data2.length; i++) {
            data2[i] = sc.nextInt();
        }

        for (int i = 0, j = 0; i < (data1.length + data2.length); i++) {
            if (i < data1.length) {
                data3[i] = data1[i];
            } else {
                data3[i] = data2[j];
                j++;
            }

        }

        for (int i = 0; i < data1.length + data2.length; i++) {
            System.out.printf("%d\n", data3[i]);
        }
    }

}
