public class Computador extends Eletrodomestico{
    Computador(boolean ligado){
        super(ligado);
    }

    @Override
    public void agir(){
        System.out.println("Computando");
    }
}
