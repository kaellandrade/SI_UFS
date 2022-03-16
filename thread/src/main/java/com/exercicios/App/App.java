package com.exercicios.App;

public class App {
    public static void main(String[] args) throws InterruptedException {
        MyArrThread arr = new MyArrThread(5);

        arr.start();

        arr.join(); // Aguardando minha Thread terminar.

        System.out.println("Array Original:");
        String originalArr = MyArrThread.formmatedArr(arr.getVector());
        System.out.println(originalArr);

        System.out.println("Array Ordenado (copia):");
        String copyAtt = MyArrThread.formmatedArr(arr.getNewVectorSort());
        System.out.println(copyAtt);
    }

}
