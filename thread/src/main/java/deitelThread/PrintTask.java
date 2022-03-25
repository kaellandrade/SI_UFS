package deitelThread;
import java.security.SecureRandom;
import java.util.Random;

public class PrintTask implements Runnable{    
    private static final SecureRandom generator = new SecureRandom();
    private final int sleepTime; // Tempo de adormecimento para uma thread
    private final String taskName;

    public PrintTask(String taskname){
        this.taskName = taskname;

        // Tempo random entre 0 e 5
        sleepTime = generator.nextInt(5000);
    }

    // método run contém o código que uma thread executará
    @Override
    public void run() {
        try { // coloca a thread para dormir pela quantidade de tempo sleepTime 

            System.out.printf("%s Vai dormir por %d milisegundos.\n", taskName, sleepTime);
            Thread.sleep(sleepTime); // coloca a thread para dormir (espera sincronizada)

        } catch (InterruptedException exceptione) {
            
            exceptione.printStackTrace();
            Thread.currentThread().interrupt(); // Reinterrompe a Thread
        }
        // Imprime o nome da tarefa
        System.out.printf("%s Done Sleeping\n", taskName);
    }
}
