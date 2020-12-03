public class Televisao {
    private int volume;
    private int canal;

    Televisao(int volume, int canal){
        this.volume = volume;
        this.canal = canal;

    }

    public int getVolume(){
        return this.volume;
    }

    public int getCanal(){
        return this.canal;
    }

    public void setVolume(int v){
        this.volume += v;
    }

    public void setCanal(int c){
        if(c < 0)
            this.canal--;
        else if(c == 1)
            this.canal++;
        else
            this.canal = c;
        
    }
    

}
