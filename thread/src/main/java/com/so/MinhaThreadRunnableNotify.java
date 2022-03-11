package com.so;

public class MinhaThreadRunnableNotify implements Runnable {
    private String nome;
    Object notificar;

    public MinhaThreadRunnableNotify(String nome, Object notificar) {
        this.nome = nome;
        this.notificar = notificar;
    }

    @Override
    public void run() {
        for (int i = 0; i < 10; i++) {
            System.out.printf("%s %d%n", this.nome, i);
            synchronized (this.notificar) {
                this.notificar.notifyAll();
            }
            /*
             * try {
             * Thread.sleep(500); // Meio segundo dormindo,depois sei de desbloqueada para
             * pronto.
             * } catch (InterruptedException e) {
             * e.printStackTrace();
             * }
             */
        }
        System.out.printf("FIM %s\n", this.nome);
    }
}
