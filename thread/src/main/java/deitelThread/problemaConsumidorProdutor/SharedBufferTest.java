package deitelThread.problemaConsumidorProdutor;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;

public class SharedBufferTest {
    public static void main(String[] args) throws InterruptedException{
        // Cria novo pool de threads com duas threads
        ExecutorService executorService = Executors.newCachedThreadPool();

        // Cria UnsynchronizedBuffer para armazenar ints
        Buffer sharedLocation = new UnsynchronizedBuffer();

        System.out.println("Action\t\tValue\tSum of produced\tSum of Cosumed");
        System.out.printf("------\t\t-----\t--------------\t--------------\n\n");

        /**
         * Executar Produce e Consumer, dando a cada um acesso a shared
         */

        executorService.execute(new Producer(sharedLocation));
        executorService.execute(new Consumer(sharedLocation));

        executorService.shutdown();//Termina o aplicativo quando as tarefas concluem
        executorService.awaitTermination(1, TimeUnit.MINUTES); 
    }
}
