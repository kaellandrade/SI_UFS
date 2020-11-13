public class Triangulo {
    private float ladoX;
    private float ladoY;
    private float ladoZ;

    public void setLadoX(float ladoX) {
        this.ladoX = ladoX;
    }

    public void setLadoY(float ladoY) {
        this.ladoY = ladoY;
    }

    public void setLadoZ(float ladoZ) {
        this.ladoZ = ladoZ;
    }

    public boolean eTriangulo() {
        if (ladoX < (ladoY + ladoZ) && ladoY < (ladoX + ladoZ) && ladoZ < (ladoX + ladoY)) {
            return true;
        }else{
            return false;
        }
    }

    public String mostraTipo(){
        if(eTriangulo()){
            if(ladoX == ladoY && ladoY == ladoZ){
                return "Equilátero";
            }else if(ladoX != ladoY && ladoY != ladoZ){
                return "Escaleno";
            }else{
                return "Isósceles";
            }
        }else{
            return "Não é triangulo";
        }
    }
}
