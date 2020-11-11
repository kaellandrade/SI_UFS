
public class Aluno {
    private float nota1;
    private float nota2;
    private float nota3;
    private float media;

    public void setNota1(float valor) {
        nota1 = valor;
    }

    public void setNota2(float valor) {
        nota2 = valor;
    }

    public void setNota3(float valor) {
        nota3 = valor;
    }

    public float calcMedia() {
        media = (nota1 + nota2 + nota3) / 3.0f;
        return media;
    }

    public String verificaAprovacao() {

        if(media < 3){
            return "Reprovado";
        }else if( media >= 3.0 && media < 7.0){
            return "Prova final";
        }else{
            return "Aprovado";
        }
    }
}