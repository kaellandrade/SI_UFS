/*
NÍVEL: Fácil
Tópicos: acumulador, dicionário 
Descrição
--------
Você terá como uma entrada várias linhas, cada uma com uma string. 
O valor de cada caracter é computado como segue: 

Valor = (Posição no alfabeto) + (Elemento de entrada) + (Posição do elemento) 

Todas posições são baseadas em zero. 'A' tem posição 0 no alfabeto, 'B' tem posição 1 no alfabeto, ... O cálculo de hash retornado é a soma de todos os caracteres da entrada. Por exemplo, se a entrada for:
CBA
DDD

então cada caractere deverá ser computado como segue:

2 = 2 + 0 + 0 : 'C' no elemento 0 posição 0
2 = 1 + 0 + 1 : 'B' no elemento 0 posição 1
2 = 0 + 0 + 2 : 'A' no elemento 0 posição 2
4 = 3 + 1 + 0 : 'D' no elemento 1 posição 0
5 = 3 + 1 + 1 : 'D' no elemento 1 posição 1
6 = 3 + 1 + 2 : 'D' no elemento 1 posição 2

O cálculo final de hash será 2+2+2+4+5+6 = 21.

Formato de entrada
------------------
A entrada contém vários casos de teste. 
A primeira linha de entrada contém um inteiro N que indica a quantidade de casos de teste. Cada caso de teste inicia com um inteiro L (1 ≤ L ≤ 100) que indica a quantidade de linhas que vem a seguir. 
Cada uma destas L linhas contém uma string com até 50 letras maiúsculas ('A' - 'Z').

Formato de saída
----------------

Para cada caso de teste imprima o valor de hash que é calculado conforme o exemplo apresentado acima.
*/
#include <stdio.h>
#include <stdlib.h>
#define LEN 50

int funchash(char *str, int elementoEntrada);
int posicaoABC(int c);

int main(void)
{
    char *palavra = malloc(sizeof(char) * LEN);
    int testes;
    int linhas;
    int hash = 0;

    scanf("%d", &testes);
    for (int i = 0; i < testes; i++)
    {
        scanf("%d", &linhas);
        hash = 0;
        for (int j = 0; j < linhas; j++)
        {
            scanf("%s", palavra);
            hash += funchash(palavra, j);
        }
        printf("%d\n", hash);
    }

    return 0;
}

int funchash(char *str, int elementoEntrada)
{
    int valor = 0;
    int i = 0;
    while (str[i] != '\0')
    {
        valor += posicaoABC(str[i]) + i + elementoEntrada;
        i++;
    }
    return valor;

}

int posicaoABC(int c)
{
    return c - 65;
}