#include <stdio.h>
#define LENGTH 5

void quemLevaBandeja(int *a, int *p, int *m, int *e, int *j, int *vet);
void imprimeDia(int *dia);
void troca(int *x, int *y);
void ordenaVetor(int *vet);

int main(void)
{
    int ambrosio, peru, minerim, entidade, jef, vet[LENGTH];
    for (int i = 0; i < LENGTH; i++)
    {
        scanf("%d", &vet[i]);
    }
    ambrosio = vet[0];
    peru = vet[1];
    minerim = vet[2];
    entidade = vet[3];
    jef = vet[4];
    ordenaVetor(&vet[0]);
    quemLevaBandeja(&ambrosio, &peru, &minerim, &entidade, &jef, &vet[0]);
    return 0;
}
void quemLevaBandeja(int *a, int *p, int *m, int *e, int *j, int *vet)
{
    int valueAtual;
    for (int i = 1; i < LENGTH; i++)
    {
        valueAtual = vet[i];
        imprimeDia(&i);
        if (*a == valueAtual)
        {
            printf("Ambrosio");
        }
        else if (*p == valueAtual)
        {
            printf("Peu");
        }
        else if (*m == valueAtual)
        {
            printf("Minerin");
        }
        else if (*e == valueAtual)
        {
            printf("Entidade");
        }
        else
        {
            printf("Jeff");
        }
        printf("\n");
    }
}
void imprimeDia(int *dia)
{
    if (*dia == 1)
        printf("Terca-feira: ");
    if (*dia == 2)
        printf("Quarta-feira: ");
    if (*dia == 3)
        printf("Quinta-feira: ");
    if (*dia == 4)
        printf("Sexta-feira: ");
}
void troca(int *x, int *y)
{
    int aux;
    aux = *x;
    *x = *y;
    *y = aux;
}
void ordenaVetor(int *vet)
{
    for (int i = 0; i < LENGTH; i++)
    {
        for (int j = 0; j < LENGTH - 1; j++)
        {
            if(vet[j] > vet[j+1]){
                troca(&vet[j], &vet[j+1]);
            }
        }
    }
}
