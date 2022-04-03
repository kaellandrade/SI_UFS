package problemaConsumidorProdutor;
import java.security.SecureRandom;

public class Consumer implements Runnable {
    private static final SecureRandom generator = new SecureRandom();
    private final Buffer sharedLocation;

    public Consumer(Buffer sharedLocation){
        this.sharedLocation = sharedLocation;
    }

    @Override
    public void run() {
        int sum = 0;

        for (int i = 1; i <=10; i++) {
            try {
                Thread.sleep(generator.nextInt(3000)); // Sleep random
                sum += sharedLocation.BlockingGet(); // ler o valor dobuffer

                System.out.printf("\t\t\t%2d\n", sum);
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
            System.out.printf("\n%s %d\n%s\n", "Consumer read values totaling",sum, "Terminating Consumer");
            
        }
        
    }

}
