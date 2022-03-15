package com.exercicios.App;

import java.util.Scanner;

import java.lang.reflect.Constructor;
import java.text.Format;
import java.util.Iterator;
import java.util.Scanner;

public class MyArr {
    private float[] vector;

    public MyArr(int length) {
        this.vector = new float[length];
    }

    public float[] getVector() {
        return vector;
    }

    public void setVector(float[] vector) {
        this.vector = vector;
    }

    public void fillVector() {
        Scanner s_vec = new Scanner(System.in);

        for (int i = 0; i < this.vector.length; i++) {
            this.vector[i] = s_vec.nextFloat();
        }
        s_vec.close();
    }

    @Override
    public String toString() {
        String res = "";
        for (int i = 0; i < this.vector.length; i++) {
            res += String.format("[%d] -> %.2f\n", i, this.vector[i]);

        }
        return res;
    }
}
