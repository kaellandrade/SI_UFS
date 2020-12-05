# Lista de Exercício 7 – Pilares da Programação Orientada a Objetos (Parte 2)
1. Crie uma classe Figura, que tem o método calcularArea(). Crie outras 3 classes,
que herdam de Figura:
    - a) Quadrado, que possui a medida de um lado, reescreve calcularArea() para
        retornar a área de um quadrado
    - b) Circulo, que possui raio e reescreve calcularArea()
    - c) Triângulo, que possui 3 lados e reescreve calcularArea()

    Sobrecarregue os construtores padrão para setar atributos iniciais diferentes de
    zero, para serem usados nos métodos calcularArea().
    Por fim, escreva uma classe com um método main que declara como objeto
    apenas uma Figura e pergunta ao usuário qual figura geométrica deseja. Após a
    leitura, imprimir o retorno da função calcularArea() para a Figura escolhida.

2. Crie uma classe Televisão e uma classe ControleRemoto, que herda de Televisão,
que pode controlar o volume e trocar os canais.
    - a) O controle de volume permite aumentar ou diminuir a potência do volume de
    som em uma unidade de cada vez.

    - b) O controle de canal também permite aumentar e diminuir o número do canal em
    uma unidade, porém, também possibilita trocar para um canal indicado

    - c) Também devem existir métodos para consultar o valor do volume de som e o
    canal selecionado.

    Criar uma classe com um main para testar e apresentar a troca de canais e
    de volume.

3. Escreva um código que represente a classe Eletrodomestico, com o atributo ligado
e o método imprimir. O método imprimir deve mostrar na tela os valores de todos
os atributos. O atributo ligado é booleano e deve indicar o estado atual do
eletrodoméstico, se ligado ou desligado.

    - a) Adicione um construtor que permita a definição de todos os atributos no
        momento da instanciação do objeto

    - b) Adicione os métodos ligar e desligar que devem mudar o conteúdo do atributo
        ligado conforme o caso e imprimir “ligando” ou “desligando”. Ligar também
        chama um método agir

    - c) Crie as classes filhas Televisão, Batedeira e Computador, com construtores que
        chamam o construtor parametrizado da classe pai e que sobrecarregam o
        método agir:
    1. agir de televisão imprime “mostrando imagem”
    2. agir de batedeira imprime “batendo”  
    3. agir de computador imprime “computando”

4. Leia o texto sobre uma loja de supermercado e implemente usando conceitos de
orientação a objetos:
    - a) Gerente e Vendedores são Empregados
    - b) Empregados e Clientes são Pessoas
    - c) Gerente tem um setor
    - d) Vendedor tem uma cota de peças para vender e só pode vender uma peça de
    - cada vez
    - e) Empregados tem salário e o salário de um vendedor é um salário-mínimo. O
    salário do Gerente são dois salários-mínimos
    - f) Clientes podem ou não ter dívida com a loja
    - g) Pessoas possuem nome, idade, telefone

    Faça um programa em Java que crie um Cliente, Vendedor e Gerente e imprima
    todos os seus atributos. Simule também uma venda e mostre a nova cota do
    vendedor.

5. Crie uma classe Animal que possui massa, tamanho (pequeno médio ou grande) e
os seguintes métodos: comunicar e movimentar.
Crie 3 classes filhas, Homem, Peixe e pássaro, que sobrecarregam esses dois
métodos.

    ## Comunicar:
    - a) Homem imprime “falando”
    - b) Peixe imprime “glub glub”
    - c) Pássaro imprime “cantando”
    ## Movimentar
    - d) Homem imprime “andando”
    - e) Peixe imprime “nadando”
    - f) Pássaro imprime “voando”

    Faça um main chamando os métodos movimentar e comunicar de Homem, Peixe e
    Planta, a partir de um objeto Animal, e imprima suas respectivas massa e tamanho.