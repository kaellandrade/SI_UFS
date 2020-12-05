public class AppAnimal {
    public static void main(String[] args){
        Animal homem = new Homem(20, "Médio");
        Animal peixe = new Peixe(9, "Pequeno");
        Animal passaro = new Passaro(5, "Pequeno");

        System.out.println(homem);
        homem.comunicar();
        homem.movimentar();

        System.out.println(peixe);
        peixe.comunicar();
        peixe.movimentar();

        System.out.println(passaro);
        passaro.comunicar();
        passaro.movimentar();
    }
}