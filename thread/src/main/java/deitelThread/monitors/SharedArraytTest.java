package deitelThread.monitors;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;

public class SharedArraytTest {
    public static void main(String[] args) {
        // Constroi o objeto compartilhado

        SimpleArray sharedSimpleArray = new SimpleArray(6);

        // Cria duas tarefas a gravar no SimpleArra compartilhado
        ArrayWriter writer1 = new ArrayWriter(1, sharedSimpleArray);
        ArrayWriter writer2 = new ArrayWriter(11, sharedSimpleArray);
        

        // Executa as tarefas com um ExecutorService
        ExecutorService executorService = Executors.newCachedThreadPool();

        executorService.execute(writer1);
        executorService.execute(writer2);
        
        executorService.shutdown();

        try {
            // Espera 1 minuto para que ambos os escritores terminem a execução
            boolean tasksEnd = executorService.awaitTermination(1, TimeUnit.MINUTES);

            if(tasksEnd){
                System.out.printf("\nContents of SimpleArray:\n");
                System.out.println(sharedSimpleArray); //imprime o conteúdo
            }else{
                System.out.println("Timed out while waiting for tasks to finish");
            }
        } catch (InterruptedException ex) {
            ex.printStackTrace();
        }
        
    }
}
