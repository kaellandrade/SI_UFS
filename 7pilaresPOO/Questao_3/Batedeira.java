public class Batedeira extends Eletrodomestico{
    Batedeira(boolean ligado){
        super(ligado);
    }

    @Override
    public void agir(){
        System.out.println("Batendo");
    }
}
