/*
NÍVEL: Médio
Tópicos: array, substrings, caractere, string, Boyer Moore

Descrição
---------
Faça um programa para ler uma string e um caracter qualquer e calcule o número de ocorrências 
desse caracter na string. Exemplo: Seja a string "maracatu" e o caracter 'a', então o número de ocorrências é 3.

Formato de entrada
------------------
Você lerá duas linhas. Na primeira linha você receberá uma string com no máximo 50 caracteres. 
Na segunda linha você receberá um único caracter.

Formato de saída
-----------------
Imprima um número inteiro indicando quantas vezes o caracter dado aparece na string.  
Depois de imprimir o número, imprima um final de linha (ou seja, pule uma linha).

EX:
maracatu  -> 3
a
*/
#include <stdlib.h>
#include <stdio.h>
#define ALFABETO 256
#define MAX_PALAVRA 200
typedef unsigned char byte;

int boyermoore1(byte *a, int *m, byte *b, int *n);
int tamanhoPalavra(byte *p);
int main()
{

    byte *texto = malloc(sizeof(byte) * MAX_PALAVRA);
    byte *palavra = malloc(sizeof(byte) * MAX_PALAVRA);

    scanf("%s", texto);
    scanf("%s", palavra);
    int m = tamanhoPalavra(palavra);
    int n = tamanhoPalavra(texto);
    --m,--n;

    printf("%d", boyermoore1(palavra, &m, texto, &n));

    return EXIT_SUCCESS;
}

int boyermoore1(byte *a, int *m, byte *b, int *n)
{
    int ult[ALFABETO] = {0}; 
    for (int i = 1; i <= (*m); ++i)
        ult[a[i]] = i;

    int ocorrs = 0;
    int k = (*m);
    while (k <= *n)
    {
        int i = (*m), j = k;
        while (i >= 0 && a[i] == b[j])
            --i, --j;
        if (i < 0)
            ++ocorrs;
        if (k == *n)
            k += 1;
        else
            k += (*m) - ult[b[k + 1]] + 1;
    }
    return ocorrs;
}
int tamanhoPalavra(byte *p)
{
    int i = 0;
    if (p[i] == '\0') return 0;
    else return tamanhoPalavra(&p[i + 1]) + 1;
}