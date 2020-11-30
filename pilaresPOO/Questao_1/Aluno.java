public class Aluno extends Pessoa {
    private float nota1;
    private float nota2;
    private float nota3;

    Aluno(){
        this.nota1 = 0f;
        this.nota2 = 0f;
        this.nota3 = 0f;
    }

    Aluno(String nome, String data, float nota1, float nota2, float nota3){
        super(nome, data);
        this.nota1 = nota1;
        this.nota2 = nota2;
        this.nota3 = nota3;
    }
    
    public void setNota1(float nota1){
        this.nota1 = nota1;
    }

    public void setNota2(float nota2){
        this.nota2 = nota2;
    }

    public void setNota3(float nota3){
        this.nota3 = nota3;
    }

    public float getNota1(){
        return this.nota1;
    }

    public float getNota2(){
        return this.nota2;
    }

    public float getNota3(){
        return this.nota3;
    }
}
