#include <stdio.h>
#include <math.h>
#include <stdlib.h>

/* DESCRIÇÃO:
------------
Crie um programa que tenha apenas uma função, além do programa principal, 
que receberá como parâmetro um número natural estritamente positivo n e que exiba, conforme o exemplo de saída, 
n linhas em que a primeira tem n valores n com hifens entre eles; a linha seguinte tem n-1 valores n-1 
novamente com hifens entre eles) e assim por diante até n-(n-1). 
O PROGRAMA PRINCIPAL deverá ler o valor de n e a FUNÇÃO deverá exibir as linhas.

Formato de entrada
5

Formato de saída
5-5-5-5-5
4-4-4-4
3-3-3
2-2
1

*/
void imprimeTriangulo(int *p);

int main()
{
    int n;
    scanf("%d", &n);
    imprimeTriangulo(&n);

    return EXIT_SUCCESS;
}


void imprimeTriangulo(int *p)
{
    int j = *p;
    while (j != 0)
    {
        for (int i = 1; i <= j; i++) // Imprime o valor de j j-vezes.
        {
            printf("%d", j);
            if (i != j)
                printf("-");
        }
        printf("\n");
        j--;
    }
    printf("\n");
}