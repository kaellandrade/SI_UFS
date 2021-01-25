/*
NÍVEL: Fácil
Descrição
----------

Imagine uma fila de pessoas esperando para serem atendidas, com prioridade para pessoas idosas (acima de 60 anos). Assim, as pessoas se dividem em duas filas distintas, uma para pessoas idosas e outra para não idosas. 
Sempre que houver disponibilidade para uma nova pessoa ser atendida, uma pessoa deve ser removida de uma das filas, de acordo com as seguintes regras:

-Caso 'n' pessoas da fila de idosos sejam atendidas de forma consecutiva enquanto existir alguém na fila de não-idosos, a próxima pessoa a ser atendida será a que está na fila de não-idosos, e a contagem de atendimentos da fila de idosos é reiniciada (mais 'n' idosos podem ser atendidos em sequência novamente, mesmo se existir alguém aguardando na fila de não-idosos). o valor de 'n' deve ser informado como uma das entradas do problema;

-Caso não exista ninguém na fila de idosos, o próximo a ser atendido é alguém da fila de não-idosos, e a contagem de idosos atendidos em sequência é zerada;

-Caso não exista ninguém na fila de não-idosos, o próximo a ser atendido é alguém da fila de idosos, e a contagem de idosos atendidos em sequência é zerada;

Formato de entrada
------------------

No início do programa, deve ser lido o valor de 'n' (prioridade para a fila de idosos) e as filas devem ser criadas. Em seguida, cada um dos caracteres poderá ser lido repetidamente para representar as seguintes operações:

'a': adiciona uma nova pessoa na fila. após o 'a' a linha seguinte deve conter o valor do identificador da pessoa (inteiro) e sua idade (inteiro);

'r': remove uma pessoa da fila (de idosos ou não-idosos) para ser atendida;

'i': imprime todos os elementos de cada uma das filas (de idosos ou não-idosos);

'f': finaliza o programa.

Formato de saída
----------------

Os dados (id e idade) de todas as pessoas das duas filas (idosos e não-idosos) devem ser impressos de acordo com o seguinte padrão: 

fila de idosos:
ID: 1 IDADE: 95
ID: 2 IDADE: 67
fila de nao-idosos:
ID: 3 IDADE: 22
----------

sendo o elemento do início da fila impresso primeiro, enquanto que o elemento do final da fila (último a ser removido) é impresso por último.
*/
