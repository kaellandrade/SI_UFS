
public class PessoaIMC extends Pessoa{
    private double peso;
    private double altura;

    PessoaIMC(String nome, String dataNascimento, double peso, double altura){
        super(nome, dataNascimento);
        this.peso = peso;
        this.altura = altura;
    }


    public double calculaIMC(double peso, double altura){
        return peso/(altura*altura);
    }

    public String resultIMC(){
        return String.valueOf(calculaIMC(this.peso, this.altura));
    }

    public String toString(){
        return "Nome: " + super.getNome() +
        "\nData de Nascimento: " + super.getDataNascimento() +
        "\nPeso: " + this.peso +
        "\nAltura: " + this.altura;
    }

    public double getPeso(){
        return this.peso;
    }
    public double getAltura(){
        return this.altura;
    }
}