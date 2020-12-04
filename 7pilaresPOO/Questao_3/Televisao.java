public class Televisao extends Eletrodomestico{
    Televisao(boolean ligado){
        super(ligado);
    }

    @Override
    public void agir(){
        System.out.println("Mostrando imagem");
    }
}
