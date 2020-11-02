#include <stdio.h>

void imprimeVetor(int *vet, int *TAMANHO);
void troca(int *x, int *y);
void ordenaVetor(int *vet, int *TAMANHO);

void main(void)
{
    int n, i, *p_n, *p_i;
    p_n = &n;
    p_i = &i;
    *p_i = 0;
    scanf("%d", p_n);
    int vet[*p_n];
    // Ler os vaalores
    while ((*p_i) < (*p_n))
    {
        scanf("%d", &vet[*p_i]);
        (*p_i)++;
    }
    ordenaVetor(&vet[0], p_n);  // Ordena meu vetor
    imprimeVetor(&vet[0], p_n); //Imprime o vetor
    return 0;
}

// Dado um vetor e seu respectivo tamanho, o vetor será impresso;
void imprimeVetor(int *vet, int *TAMANHO)
{
    for (int i = 0; i < (*TAMANHO); i++)
    {
        printf("[%d]", vet[i]);
    }
    printf("\n");
}

// Dado troca os valores de *x e *y
void troca(int *x, int *y)
{
    int aux;
    aux = *x;
    *x = *y;
    *y = aux;
}

// Dado um vetor e seu respectivo tamanho, este vetor será ordenado
// usando o bublesort
void ordenaVetor(int *vet, int *TAMANHO)
{
    int j, *p_j;
    p_j = &j;
    *p_j = 0;
    for (int i = 0; i < (*TAMANHO); i++)
    {
        *p_j = 0;
        while (*p_j < (*TAMANHO) - 1)
        {
            if (vet[*p_j] > vet[(*p_j) + 1])
                troca(&vet[(*p_j)], &vet[(*p_j) + 1]);
            (*p_j)++;
        }
    }
}