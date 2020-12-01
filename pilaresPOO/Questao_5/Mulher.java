public class Mulher extends PessoaIMC{


    Mulher(String nome, String dataNascimento, double peso, double altura){
        super(nome, dataNascimento, peso, altura);
    }
    
    @Override
    public String resultIMC() {
        double imc = calculaIMC(super.getPeso(), super.getAltura());
        if(imc < 19f)
            return "Abaixo do peso ideal";
        else if(imc >= 19f && imc <= 25.8f)
            return "Peso ideal";
        else
            return "Acima do peso";
    }
}
