package com.so;

public class MinhaThread extends Thread {
    private String nome;

    public MinhaThread(String nome) {
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
