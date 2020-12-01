import java.util.Random;

public class Oficina {
    
    public Veiculo proximo(){
        Veiculo vec;

        Random r = new Random();
        int valor = r.nextInt(2);

        if(valor == 0)
            vec = new Automovel();
        else
            vec = new Bicicleta();
        return vec;
    }

    public void manutencao(Veiculo v){
        System.out.printf("%s\n%s\n%s\n", v.listarVerificacoes(), v.ajustar(), v.limpar());
        if(v.getClass().getName() == "Automovel"){
            System.out.println(v.mudarOleo());
        }

    }
    
}
