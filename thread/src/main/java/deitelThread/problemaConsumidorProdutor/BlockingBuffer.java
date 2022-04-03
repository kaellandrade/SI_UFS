package deitelThread.problemaConsumidorProdutor;

import java.util.concurrent.ArrayBlockingQueue;

public class BlockingBuffer implements Buffer {

    private final ArrayBlockingQueue<Integer> buffer; // buffer conpartilhado

    public BlockingBuffer() {
        buffer = new ArrayBlockingQueue<Integer>(1);
    }

    @Override
    public void BlockingPut(int value) throws InterruptedException {

        buffer.put(value); // Coloca o valor no buffer

        System.out.printf("%s%2d\t%s%d%n","Producer writes ", value, "Buffer cells occupied: ", buffer.size());
    }

    @Override
    public int BlockingGet() throws InterruptedException {
        int readValue = buffer.take(); // Remove o valor do buffer

        System.out.printf("%s %2d\t%s%d%n", "Conssumer reads ", readValue, "Buffer cells occupied: ", buffer.size());

        return readValue;
    }

}
