public class Homem extends PessoaIMC{

    Homem(String nome, String dataNascimento, double peso, double altura){
        super(nome, dataNascimento, peso, altura);
    }

    @Override
    public String resultIMC() {
        double imc = calculaIMC(super.getPeso(), super.getAltura());
        if(imc < 20.7)
            return "Abaixo do peso ideal";
        else if(imc >= 20.7 && imc <= 26.4)
            return "Peso ideal";
        else
            return "Acima do peso";
    }
}
