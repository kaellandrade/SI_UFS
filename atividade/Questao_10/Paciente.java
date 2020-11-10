public class Paciente {
    private String nome;
    private float peso;
    private float altura;
    private char sexo;
    private int idade;

    public void setNome(String paciente) {
        nome = paciente;
    }

    public void setPeso(float kg) {
        peso = kg;
    }

    public void setAltura(float alt) {
        altura = alt;
    }

    public void setSexto(char c) {
        sexo = c;
    }

    public void setIdade(int anos) {
        idade = anos;
    }

    public String getNome(){
        return nome;
    }

    public float getPeso(){
        return peso;
    }

    public float getAltura(){
        return altura;
    }

    public char getSexo(){
        return sexo;
    }

    public int getIdade(){
        return idade;
    }

    public float calcularConsulta(){
        return altura * peso + idade;
    }
}
