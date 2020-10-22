#include <stdio.h>
#include <math.h>
#include <stdlib.h>
struct ponto
{
    int x;
    int y;
};

int r(int *x, int *y);
int b(int *x, int *y);
int c(int *x, int *y);
void imprimeCamp(struct ponto value);
void lerVetor(struct ponto *p);

int main()
{
    int inputs;
    scanf("%d", &inputs);
    struct ponto vet[inputs];

    for (int i = 0; i < inputs; i++)
    {
        scanf("%d%d", &vet[i].x, &vet[i].y);
    }

    return 0;
}

// Função do rafael
int r(int *x, int *y)
{
    return pow(3 * (*x), 2) + pow(*y, 2);
}

// Função do beto
int b(int *x, int *y)
{
    return 2 * pow(*x, 2) + pow(5 * (*y), 2);
}

// Função do carlos
int c(int *x, int *y)
{
    return -100 * (*x) + pow(*y, 3);
}