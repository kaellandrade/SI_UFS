#include <stdio.h>
#include <stdlib.h>
void imprimeVetor(int *vet, int *TAMANHO);
void troca(int *x, int *y);
void ordenaVetor(int *vet, int *TAMANHO);

int main(void)
{
    int n, i, *p_n, *p_i;
    p_n = &n;
    p_i = &i;
    *p_i = 0;
    scanf("%d", p_n);
    int vet[*p_n];
    // Ler os valores
    while ((*p_i) < (*p_n)) // Enquanto meu contador i for menor que o total de leituras
    {
        scanf("%d", &vet[*p_i]);
        (*p_i)++;
    }
    ordenaVetor(vet, p_n);  // Ordena meu vetor
    imprimeVetor(vet, p_n); //Imprime o vetor
    return EXIT_SUCCESS;
}

// Dado um vetor (por referência) e seu respectivo tamanho, o vetor será impresso
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

// Dado um vetor (por referência) e seu respectivo tamanho, o vetor será ordenado
// usando o bubblesort
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