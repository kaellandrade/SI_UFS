#include <stdio.h>
#include <stdlib.h>
/*DESCRIÇÃO
-----------
O jovem Ambrósio estava decifrando uma mensagem escrevendo letra por letra em pedaços de papel. 
Em cada pedaço Ambrósio escreveu uma letra e um número representando sua posição, da seguinte forma:
1 M
2 e
3 n
4 s
5 a
6 g
7 e
8 m
Porém Ambrósio esbarrou na mesa e bagunçou todos os pedaços. Ajude-o a reorganizar a mensagem.



Formato de entrada:
Um inteiro N representando a quantidade de pedaços. (0 < N < 200)
N linhas contendo um inteiro M e um caractere C. (1 < M <= N)

Formato de saída
Todos os caracteres dos pedaços na ordem correta.

Exemplo de entrada:
19
1 h
8 t
2 o
18 p
3 j
12 r
13 o
5 v
16 d
6 a
11 p
15 a
9 e
17 e
14 v
7 i
10 r
19 1
4 e

Exemplo de saída:
hojevaiterprovadep1
*/

int main(void)
{

    int total, *p_total, posicao, *p_posicao;
    char *p_letra, letra;
    p_letra = &letra;
    p_total = &total;
    p_posicao = &posicao;
    // Ler a quantidade de pedaços 
    scanf("%d", p_total);
    char palavra[*p_total]; // define um vetor com o total de pedaços

    // um caractere e sua posição  
    for (int i = 0; i < (*p_total); i++)
    {
        scanf("%d %c", p_posicao, p_letra);
        palavra[*p_posicao - 1] = *p_letra; // dado um número x e um caractere j, palavra[x-1]=j
    }
    printf("%s\n", palavra);
    return EXIT_SUCCESS;
}