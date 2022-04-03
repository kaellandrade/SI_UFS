package com.exercicio.pratica;

import java.util.Arrays;
import java.util.Scanner;

public class MyArrThread extends Thread {
    private float[] vector;
    private float[] newVectorSort;

    public MyArrThread(int length) {
        this.vector = new float[length];
        this.newVectorSort = new float[length];
    }

    private void sortVector() {
        Arrays.sort(this.newVectorSort);
    }

    public float[] getVector() {
        return this.vector;
    }

    public float[] getNewVectorSort() {
        return this.newVectorSort;
    }

    public void setVector(float[] vector) {
        this.vector = vector;
    }

    /**
     * Preeenche o vetor.
     */
    private void fillVector() {
        Scanner s_vec = new Scanner(System.in);

        for (int i = 0; i < this.vector.length; i++) {
            float number = s_vec.nextFloat();

            this.vector[i] = number;
            this.newVectorSort[i] = number;

        }
        s_vec.close();
    }

    @Override
    public void run() {
        this.fillVector();
        this.sortVector();
    }

    static public String formmatedArr(float[] arr) {
        String res = "";
        for (int i = 0; i < arr.length; i++) {
            res += String.format("[%d] -> %.2f\n", i, arr[i]);
        }
        return res;
    }
}
