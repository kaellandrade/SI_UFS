package com.exercicios.App;

import java.util.Scanner;

public class App {
    private static Scanner std_answer;

    public static void main(String[] args) throws InterruptedException {
        char answer = 'y';
        std_answer = new Scanner(System.in);

        do {

            System.out.println("Digite o tamanho do vetor1: ");
            MyArrThread arr = new MyArrThread(std_answer.nextInt());

            arr.start();
    
            arr.join(); // Aguardando minha Thread terminar.

            System.out.println("Array Original:");
            String originalArr = MyArrThread.formmatedArr(arr.getVector());
            System.out.println(originalArr);

            System.out.println("Array Ordenado (copia):");
            String copyAtt = MyArrThread.formmatedArr(arr.getNewVectorSort());
            System.out.println(copyAtt);

            System.out.println("---Deseja repetir o processo?---");
            answer = std_answer.next().charAt(0);

        } while (answer == 'y');
        std_answer.close();

    }

}
