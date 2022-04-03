package deitelThread.problemaConsumidorProdutor;
import java.security.SecureRandom;

public class Producer implements Runnable {
    private static final SecureRandom generator = new SecureRandom();
    private final Buffer sharedLocation;

    public Producer(Buffer sharedLocation){
        this.sharedLocation = sharedLocation;
    }

    @Override
    public void run() {
        int sum = 0;

        for (int i = 1; i <=10; i++) {
            try {
                Thread.sleep(generator.nextInt(3000)); // Sleep random
                sharedLocation.BlockingPut(i); // configura valor no buffer
                sum += i; // incrementa a soma de valores
                // System.out.printf("\t%2d%n", sum);
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
            
        }
        System.out.printf("Producer done producing%nTerminating Producer%n");
        
    }

}
