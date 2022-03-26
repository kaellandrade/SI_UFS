package deitelThread.monitors;

import java.security.SecureRandom;
import java.util.Arrays;
/**
 * Classe que gerencia um array de inteirios para ser compoartilhado por várias
 * threads
 * NÃO SEGURO PARA THREADS
 */
public class SimpleArray {
    private static final SecureRandom generator = new SecureRandom();
    private final int[] array; // Array de inteiros compartilhados
    private int writeIndex = 0; // Índice compartilhado do próximo elemento a gravar

    public SimpleArray(int size) {
        array = new int[size];
    }

    public synchronized void add(int value) { // méotodo atômico (uma thread pode obter o bloqueio por vez)
        int position = writeIndex; // Armazena o indíce de gravação;

        try {
            // Coloca a thread que chamo add para dormir entre 0 a 499 segundos
            Thread.sleep(generator.nextInt(5000));
        } catch (InterruptedException ex) {
            Thread.currentThread().interrupt(); // reinterrompe a thread
        }

        // Coloca o valor no elemento apropriado
        array[position] = value;
        System.out.printf("%s wrote %2d to element%d.\n",
                Thread.currentThread().getName(), value, position);

        ++writeIndex; // Índice de eincremento de elemento a ser gravado depois
        System.out.printf("next write index: %d\n", writeIndex);
    }

    @Override
    public String toString() {
        return Arrays.toString(array);
    }
}
