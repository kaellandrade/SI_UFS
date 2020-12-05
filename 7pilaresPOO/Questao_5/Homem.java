public class Homem extends Animal{

    Homem(float massa, String tamanho){
        super(massa, tamanho);
    }

    public void comunicar(){
        System.out.println("Falando");
    }

    public void movimentar(){
        System.out.println("Andando");
    }

    public String toString(){
        return String.format("***Homem***\nTamanho: %s\nMassa: %.2f",
            super.getTamanho(), super.getMassa());
    }
    
}
