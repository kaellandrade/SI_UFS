#include <stdio.h>
#include <stdlib.h>
/*
    Definindo o algoritmo de ordenação bubblesort com ponteios;
*/

void trocavalores(int *x, int *y);
void lerVetor(int *p, int tamanhoVet);
void imprimeVetor(int *p, int tamanhoVet);
void bubblesort(int *p, int tamanhoVet);

int main()
{
    int LENGTH;
    printf("Digite o tamanho do seu vetor :)\n");
    scanf("%d", &LENGTH);

    int vet[LENGTH];

    lerVetor(vet, LENGTH);     // Ler meu vetor
    imprimeVetor(vet, LENGTH); // Imprime o vetor antes da ordenação
    bubblesort(vet, LENGTH); // Ordena meu vetor
    imprimeVetor(vet, LENGTH); // Imprime o vetor depois da ordenação
    return 0;
}

// Preenche um dado vetor dada sua posição na mémória e seu respectivo tamanho 
void lerVetor(int *p, int tamanhoVet)
{
    for (int i = 0; i < tamanhoVet; i++)
    {
        scanf("%d", &p[i]);
    }
}

// Imprime um dado vetor dada sua posição na mémória e seu respectivo tamanho  
void imprimeVetor(int *p, int tamanhoVet)
{
    printf("\n");
    for (int i = 0; i < tamanhoVet; i++)
    {
        printf("|%d|", p[i]);
    }
    printf("\n");
}

// Dado dois valores, são trocados caso x seja > y
void trocavalores(int *x, int *y)
{
    int aux;
    if (*x > *y)
    {
        aux = *x;
        *x = *y;
        *y = aux;
    }
}

// Dado um vetor p e seu tamhno, buublesort irá ordená-lo
void bubblesort(int *p, int tamanhoVet)
{
    for (int i = 0; i < tamanhoVet; i++)
    {
        for (int j = 0; j < tamanhoVet - 1; j++)
        {
            trocavalores(&p[j], &p[j+1]);
        }
        
    }
}