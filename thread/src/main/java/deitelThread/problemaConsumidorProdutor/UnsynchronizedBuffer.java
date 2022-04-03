package problemaConsumidorProdutor;

public class UnsynchronizedBuffer implements Buffer {
    private int bufer = -1; // compartilhado pelas threads producer e consumer

    /**
     * Colcoa o valor no buffer
     */
    @Override
    public void BlockingPut(int value) throws InterruptedException {
        System.out.printf("Producer writes\t%2d", value);
        bufer = value;
    }

    /**
     * Retorna valor do buffer
     */
    @Override
    public int BlockingGet() throws InterruptedException {
        System.out.printf("Consumer reads \t%2d", bufer);
        return 0;
    }
    
}
