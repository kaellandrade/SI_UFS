package com.so;

public class MinhaThreadRunnable implements Runnable {
    private String nome;

    public MinhaThreadRunnable(String nome) {
        this.nome = nome;
    }

    @Override
    public void run() {
        for (int i = 0; i < 10; i++) {
            System.out.printf("%s %d%n", this.nome, i);
        }
        System.out.printf("FIM %s\n", this.nome);
    }
}
