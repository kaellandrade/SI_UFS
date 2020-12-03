public class ControleRemoto extends Televisao{

    ControleRemoto(int volume, int canal){
        super(volume, canal);
    }

    public void aumentarVolume(){
        super.setVolume(1);
    }

    public void diminuirVolume(){
        super.setVolume(-1);
    }

    public void mudarCanal(int n){
        super.setCanal(n);        
    }
    
}
