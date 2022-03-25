package deitelThread;
import java.util.concurrent.Executors;
import java.util.concurrent.ExecutorService;

public class TaskExecutor {
    public static void main(String[] args) {
        // cria e nomeia cada executável
        PrintTask task1 = new PrintTask("Task1");
        PrintTask task2 = new PrintTask("Task2");
        PrintTask task3 = new PrintTask("Task3");

        System.out.println("Iniciando o método executor");

        //(Pool Threads) Cria ExecutorService para gerenciar as threads
        ExecutorService executorService = Executors.newCachedThreadPool();

        
        // Inicia as três printTasks
        executorService.execute(task1);
        executorService.execute(task2);
        executorService.execute(task3);

        /**
         * FECHA EXECUTORSERVICE -- ELE DECIDE QUANDO FECHAR AS THREADS
         * notificará o ExecutorService para parar de aceitar
         * novas tarefas, mas continua executando as tarefas que já foram submetidas
         */
        executorService.shutdown();

        System.out.printf("Tarefas iniciadas, main end.\n\n");
        

    }
    
}
