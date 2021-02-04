/**
 * LGORITMO DE BOYER MOORE
 * Referências: https://www.ime.usp.br/~pf/algoritmos/aulas/strma.html
 * */
#include <stdlib.h>
#include <stdio.h>
#define ALFABETO 256
#define MAX_PALAVRA 1000

typedef unsigned char byte;

int boyermoore1(byte *a, int m, byte *b, int n);
int tamanhoPalavra(byte *p);
int main()
{

    byte *texto = malloc(sizeof(byte) * MAX_PALAVRA);
    byte *palavra = malloc(sizeof(byte));

    scanf("%[^\n]%*c", texto);
    scanf("%[^\n]%*c", palavra);

    int m = tamanhoPalavra(palavra);
    int n = tamanhoPalavra(texto);

    printf("%d\n", boyermoore1(palavra, m-1, texto, n-1));


    return EXIT_SUCCESS;
}

/**
 * Recebe dois vetores a(palavra) b (texto) e seus respectivos tamanhos;
*/
int boyermoore1(byte *a, int m, byte *b, int n)
{
    int ult[ALFABETO] = {0}; // o alfabeto ? 0..255, e nicializa o vetor utf

    // preenche o vetor considerando o tamanho da palavra
    for (int i = 1; i <= m; ++i)
        ult[a[i]] = i;
    int k = m;
    while (k <= n)
    {
        int i = m, j = k;
        if(a[i] == b[j])
            return k;

        if (k == n)
            k += 1;
        else
            k += m - ult[b[k + 1]] + 1;
    }
    return -1;
}
/**
 * Dado um vetor de bytes ser? contatdo o tamanho do vetor at? uma quebra de linha
*/

int tamanhoPalavra(byte *p){
    int i = 0;
    if (p[i] == '\0') 
        return 0;
    else 
        return tamanhoPalavra(&p[i + 1]) + 1;
}
