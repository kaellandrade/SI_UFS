public class Animal {
    private float massa;
    private String tamanho;

    Animal(float massa, String tamanho){
        this.massa = massa;
        this.tamanho = tamanho;
    }
    
    public void comunicar(){
        System.out.println("Comunicando...");
    }

    public void movimentar(){
        System.out.println("Movimentando...");
    }

    public float getMassa() {
        return massa;
    }
    public String getTamanho() {
        return tamanho;
    }

    public String toString(){
        return String.format("Tamanho: %s\nMassa: %.2f", this.tamanho, this.massa);
    }
}
