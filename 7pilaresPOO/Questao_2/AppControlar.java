public class AppControlar {
    public static void main(String[] args){
        ControleRemoto ctr = new ControleRemoto(2, 50);

        System.out.println(ctr.getVolume());

        ctr.aumentarVolume();
        ctr.aumentarVolume();
        ctr.aumentarVolume();

        ctr.diminuirVolume();
        ctr.diminuirVolume();

        ctr.mudarCanal(2);
        
        System.out.println("VOLUME: "+ctr.getVolume());
        System.out.println("CANAL: "+ctr.getCanal());


    }
}
