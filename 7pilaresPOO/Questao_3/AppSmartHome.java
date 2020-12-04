public class AppSmartHome {
    public static void main(String[] args){
        Eletrodomestico eletros [] = new Eletrodomestico[3];

        eletros[0] = new Televisao(false);
        eletros[1] = new Batedeira(false);
        eletros[2] = new Computador(false);

        for(int i = 0; i < 3; i++){
            eletros[i].ligar();
            eletros[i].desligar();
        }
        
    }
}
