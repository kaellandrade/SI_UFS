# Lista de Exercícios 4 – Classes e Objetos

1. Implemente a Classe Livro com atributos para representar o código, nome e
quantidade de exemplares ✅
    - a) Crie o construtor (com todos os atributos)
    - b) Crie os métodos de acesso e modificadores
    - c) Crie uma nova classe chamada AppLivros
        - 1. Crie 3 instâncias da classe Livro
        - 2. Imprima o número de exemplares de cada livro
        - 3. Altere as quantidades e imprima novamente o número de exemplares.

2. Implemente as Classes Produto e Item com os seguintes atributos: ✅
- a) Produto: código, nome, quantidade em estoque e preço unitário
- b) Item: código, Produto, quantidade vendida
- c) Crie o construtor para cada classe
- d) Crie os métodos de acesso e modificadores para cada atributo de cada classe
- e) Crie uma nova classe chamada Venda
    - 1. Crie 2 instâncias da classe Produto
    - 2. Imprima a quantidade em estoque da cada produto ok
    - 3. Crie 3 instâncias da classe Item ok
    - 4. Imprima a quantidade do Estoque dos 2 produtos após a venda dos itens 
    - 5. Imprima para cada Item qual foi o produto vendido, a quantidade vendida,
    - preço unitário e o valor pago na venda

3. Crie uma classe Funcionário. Ele deve ter o nome do funcionário, sexo,
departamento onde trabalha e seu salário. ✅

- a) Você deve criar métodos de acesso e modificadores para cada um dos atributos
- b) Criar um método que bonifique um funcionário, que aumenta o salário do
- funcionário de acordo com o parâmetro passado como argumento.
- c) Criar também um método para calcular o ganho anual, que não recebe
    parâmetro algum, devolvendo o valor do salário multiplicado por 13.
- d) Fazer uma classe AppFuncionario para testar as funcionalidades de bonificar e
calcular o ganho anual.

4. Crie uma classe Produto. Sua classe deverá conter os seguintes atributos e
métodos: ✅
    - a) nome, precoCusto e precoVenda.
    - b)Crie métodos de acesso e modificadores para os atributos acima
    - c) No método setPrecoVenda(), fazer o tratamento para que o preço de venda não
    seja inferior ao preço de custo. Caso isso aconteça, exiba uma mensagem
    alertando o usuário.
    - d) Crie um método chamado calcularMargemLucro() que calculará a margem de
    lucro do produto.
    - e) Crie um método chamado getMargemLucroPorcentagem() que retornará a
    margem de lucro como percentual.
    - f) Criar na uma nova classe AppVendas
        - 1. Criar 3 objetos do tipo Produto
        - 2. Peça para o usuário informar os preços de custo e de venda para cada um
            deles e exiba a margem de lucro em moeda e em percentual.

5. Escreva uma classe Conta que contenha o nome do cliente, o número da conta, o
saldo e o seu limite. Estes valores deverão ser informados no construtor, sendo
que o limite não poderá ser maior que um salário-mínimo (R$ 940,00). ✅

    - a) Crie um método para depósito e um método para saque. O método de sacar
    devolverá true ou false, dependendo se o cliente pode retirar.
    - b) Crie uma classe AppConta
        - 1. Mostre o nome e o saldo de um cliente
        - 2. Faça uma operação de depósito
        - 3. Faça uma operação de saque e mostre o novo saldo, se puder
