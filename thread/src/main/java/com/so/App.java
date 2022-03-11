package com.so;

public class App {
    public static void main(String[] args) throws InterruptedException {
        Object notificacao = new Object();

        // Example 1
        MinhaThread threadA = new MinhaThread("Thread1");
        MinhaThread threadB = new MinhaThread("Thread2");

        // threadA.start();
        // threadB.start();

        // Example 2
        MinhaThreadRunnable threadARunnable = new MinhaThreadRunnable("Thread1");
        MinhaThreadRunnable threadBRunnable = new MinhaThreadRunnable("Thread2");

        Thread a = new Thread(threadARunnable);
        Thread b = new Thread(threadBRunnable);

        // a.start();
        // b.start();

        // a.join();
        // b.join();

        // Example 3
        MinhaThreadRunnableNotify threadARunnableNotify = new MinhaThreadRunnableNotify("Thread1", notificacao);
        MinhaThreadRunnableNotify threadBRunnableNotify = new MinhaThreadRunnableNotify("Thread2", notificacao);

        Thread notifyA = new Thread(threadARunnableNotify);
        Thread notifyB = new Thread(threadBRunnableNotify);

        notifyA.start();
        notifyB.start();

        // Aguarda no máximo 1 segundo até ser notificado
        for (int i = 0; i < 20; i++) {
            synchronized (notificacao) {
                notificacao.wait(1000);
            }
            System.out.println("Alguma Thread entrou em execução");

            if (!notifyA.isAlive() && !notifyB.isAlive()) {
                break;
            }

        }

        System.out.println("Fim do Main");

    }
}
