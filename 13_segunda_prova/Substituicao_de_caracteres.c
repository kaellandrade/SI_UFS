/**
NÍVEL: Fácil
Tópicos: array, substrings, caractere 
Descrição
---------
Faça um programa que leia uma string e dois caracteres. 
Troque todas as ocorrências do primeiro caracter pelo segundo. 
Exemplo: Seja a string "maracatu" e os caracteres 'a' e 'o', então a string ficará "morocotu".

Formato de entrada

Você receberá 03 linhas:
    Primeira linha: a string
    Segunda linha: o primeiro caracter
    Terceira linha: o segundo caracter

A string possui no máximo 100 caracteres.

Formato de saída
----------------
Imprima a palavra resultante da substituição dos caracteres na string original. 
Imprima um final de linha depois da palavra.

Referências: https://www.ime.usp.br/~pf/algoritmos/aulas/strma.html
*/

#include <stdlib.h>
#include <stdio.h>
#define ALFABETO 256
#define MAX_PALAVRA 100

typedef unsigned char byte;

void boyermoore1(byte *a, int m, byte *b, char *subst, int n);
int tamanhoPalavra(byte *p);
byte *texto;

int main()
{

    texto = malloc(sizeof(byte) * MAX_PALAVRA);
    byte *letraFIND = malloc(sizeof(byte));
    char letraSUBST;

    scanf("%[^\n]%*c", texto);
    scanf("%[^\n]%*c", letraFIND);
    scanf("%c", &letraSUBST);


    int m = tamanhoPalavra(letraFIND);
    int n = tamanhoPalavra(texto);
    
    boyermoore1(letraFIND, m-1, texto, &letraSUBST, n-1);

    printf("%s", texto);
    printf("\n");

    return EXIT_SUCCESS;
}


void boyermoore1(byte *a, int m, byte *b, char *subst, int n)
{
    int ult[ALFABETO] = {0}; 

    for (int i = 1; i <= m; ++i)
        ult[a[i]] = i;
    int k = m;
    while (k <= n)
    {
        int i = m, j = k;
        if(a[i] == b[j])
            b[k] = subst[0];

        if (k == n)
            k += 1;
        else
            k += m - ult[b[k + 1]] + 1;
    }
}


int tamanhoPalavra(byte *p){
    int i = 0;
    if (p[i] == '\0') 
        return 0;
    else 
        return tamanhoPalavra(&p[i + 1]) + 1;
}
