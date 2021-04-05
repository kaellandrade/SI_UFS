#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#define TOTAL 6
/**
Faça um algoritmo que leia 6 valores. A seguir, mostre a quantidade
de valoes positivos digitados;
*/

float isPositive(float x);

int main()
{
    float *valores, totalPositivos;
    totalPositivos = 0;
    valores = malloc(sizeof(float) * TOTAL);

    for (int i = 0; i < TOTAL; i++)
    {
        scanf("%f", &valores[i]);
        if (isPositive(valores[i]))
        {
            ++totalPositivos;
        }
    }
    printf("TOTAL POSITIVOS: %.2f \n", totalPositivos);
    return 0;
}

float isPositive(float x)
{
    return x >= 0;
}