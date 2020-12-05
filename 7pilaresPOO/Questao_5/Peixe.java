public class Peixe extends Animal{
    Peixe(float massa, String tamanho){
        super(massa, tamanho);
    }

    public void comunicar(){
        System.out.println("Glub Glub");
    }

    public void movimentar(){
        System.out.println("Nadando");
    }
    public String toString(){
        return String.format("***Peixe***\nTamanho: %s\nMassa: %.2f",
             super.getTamanho(), super.getMassa());
    }
}
