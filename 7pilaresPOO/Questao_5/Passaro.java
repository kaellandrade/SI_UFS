public class Passaro extends Animal{
    Passaro(float massa, String tamanho){
        super(massa, tamanho);
    }

    public void comunicar(){
        System.out.println("Cantando");
    }

    public void movimentar(){
        System.out.println("Voando");
    }
    public String toString(){
        return String.format("***Passaro***\nTamanho: %s\nMassa: %.2f", 
            super.getTamanho(), super.getMassa());
    }
}
