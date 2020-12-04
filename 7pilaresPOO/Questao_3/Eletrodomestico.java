public class Eletrodomestico {
    private boolean ligado;

    Eletrodomestico(boolean ligado){
        this.ligado = ligado;
    }

    public boolean imprimir(){
        System.out.println(this.ligado);
        return this.ligado;
    }  

    public void ligar(){
        System.out.println("Ligando...");
        agir();
        this.ligado = true;
    }
    public void desligar(){
        System.out.println("Desligando...");
        this.ligado = false;
    }
    public void agir(){
        System.out.println("Agindo...");
    }

}
