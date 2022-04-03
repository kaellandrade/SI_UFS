package deitelThread.problemaConsumidorProdutor;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;

public class BlockingBufferTest {
    public static void main(String[] args) throws InterruptedException{

        ExecutorService executorService = Executors.newCachedThreadPool();

        Buffer sharedBuffer = new BlockingBuffer();

        executorService.execute(new Producer(sharedBuffer));
        executorService.execute(new Consumer(sharedBuffer));
       
        executorService.shutdown();
        executorService.awaitTermination(1, TimeUnit.MINUTES);
        
    }
}
