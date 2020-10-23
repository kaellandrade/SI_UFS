#include <stdio.h>
#include <math.h>
#include <stdlib.h>
int r(int *x, int *y);
int b(int *x, int *y);
int c(int *x, int *y);
void imprimeCamp(int *rafael, int *beto, int *carlos);
void repImprimir(int *p);

int main(){
    int inputs;
    scanf("%d", &inputs);
    repImprimir(&inputs);
    return 0;
}

// Função do rafael
int r(int *x, int *y){
    return pow(3* (*x), 2) + pow(*y, 2);
}

// Função do beto
int b(int *x, int *y){
    return 2 * pow(*x, 2) + pow(5 * (*y), 2);
}

// Função do carlos
int c(int *x, int *y)
{
    return  pow(*y, 3) - 100 * (*x);
}

void imprimeCamp(int *r, int *b, int *c){
    if (*r > *b && *b > *c)
    {
        printf("Rafael ganhou\n");
    }
    else if (*b > *c)
    {
        printf("Beto ganhou\n");
    }
    else
    {
        printf("Carlos ganhou\n");
    }
}

void repImprimir(int *p){
    while (*p > 0)
    {
        int x;
        int y;

        scanf("%d%d", &x, &y);

        int rafael = r(&x, &y);
        int beto = b(&x, &y);
        int carlos = c(&x, &y);
        imprimeCamp(&rafael, &beto, &carlos);

        (*p)--;
    }
}