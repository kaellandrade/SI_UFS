#include<stdio.h>
#define LENGTH 3

/*
Faça um programa que preencha um vetor com oito números inteiros, calcule e mostre dois vetores
resultantes. O primeiro vetor resultante deve conter os números positivos e o segundo, os números
negativos. Cada vetor resultante vai ter, no máximo, oito posições, que não poderão ser completamente
utilizada
*/
int vetor1[LENGTH];
int positivo[LENGTH];
int negativo[LENGTH];
int contaPositivos, contaNegativos;

int main()
{
    // Preenchendo o vetor1
    contaNegativos = 0;
    contaPositivos = 0;
    for(int i=0; i<LENGTH; i++)
    {
        printf("Digite o %d valor: \n",i+1);
        scanf("%d",&vetor1[i]);

        if(vetor1[i]>=0){
            positivo[i-contaNegativos] = vetor1[i]; // [i - contaNegativos] é usado para add valores no início do vetor.
            contaPositivos++;
        }else{
            negativo[i-contaPositivos] = vetor1[i]; // [i - contaPositivos] é usado para add valores no início do vetor.
            contaNegativos++;
        }
    }

    printf("------Positivos--------\n");
    // Mostra os positivos
    for (int i = 0; i < contaPositivos; i++)
    {
        printf("%d\n",positivo[i]);
    }
    
    printf("------Negativos--------\n");
    // Mostra os negativos
    for (int i = 0; i < contaNegativos; i++)
    {
        printf("%d\n",negativo[i]);
    }

    return 0;
}
