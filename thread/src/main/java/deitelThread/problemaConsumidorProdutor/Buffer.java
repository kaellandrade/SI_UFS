package problemaConsumidorProdutor;

public interface Buffer  {
    // Colcoa o valor int no Buffer
    public void BlockingPut(int value)  throws InterruptedException;

    // retorna o valor int a partir do Buffer
    public int BlockingGet() throws InterruptedException;
}