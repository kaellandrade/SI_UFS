public class Cliente extends Pessoa {
    private boolean divida;
    Cliente( String nome, int idade, String telefone, boolean divida){
        super(nome, idade, telefone);
        this.divida = divida;
    }

    public String toString(){
        return String.format("-------\nCliente: %s\nIdade: %d\nTelefone: %s\nPendência: %s", 
        super.getNome(), super.getIdade(), super.getTelefone(), divida);
    }
}
