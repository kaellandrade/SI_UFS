/*
NÍVEL: Médio
Tópicos: busca binária 

Descrição
---------

O Sr. Indeciso está organizando um evento, ele planeja expor vários tipos de dinheiros. A organização do evento já deixou os dinheiros ordenados de forma crescente, como ele pediu. 
Mas a organização do evento está ficando estressada com as várias requisições malucas dele. Em cada uma dessas requisições, ele escolhe um valor x, e pede para que seja colocada uma corda no primeiro dinheiro maior ou igual a x, e no último dinheiro menor ou igual a x.
Antes que isso gere uma grande confusão, faça um programa que ajude a organização do evento a determinar em quais posições eles devem colocar as cordas para cada requisição maluca do Sr. Indeciso.

Formato de entrada
------------------

A primeira linha da entrada terá um inteiro n (1 <= n <= 10^5), representando a quantidade de dinheiros que serão expostos.
Na linha seguinte, terão n inteiros d_i (1 <= d_i <= 10^5), com o valor dos dinheiros na ordem crescente.
Em seguida, terá um inteiro q (1 <= q <= 10^5), representando a quantidade de requisições que o Sr. Indeciso vai fazer.
Cada uma das próximas q linhas terá um inteiro x (min(d_i) <= x <= max(d_i)), com o valor da requisição maluca.

Formato de saída
----------------
Para cada requisição maluca, você deve imprimir dois inteiros lo, hi, representando resptectivamente a posição da corda do primeiro dinheiro maior ou igual a x, e do último dinheiro menor ou igual a x.
(Observação: Note que é possível que lo > hi)

*/