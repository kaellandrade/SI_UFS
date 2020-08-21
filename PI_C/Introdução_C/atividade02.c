/*
Escreva um programa que imprima a soma de todos os números de 1 até
100. Ou seja, ele calculará o resultado de 1 + 2 + 3 + 4 + ... +100.
 */
#include<stdlib.h>
#include<stdio.h>

#define INICIO 1
#define FIM 100
int soma = 0;

int main(void){
    for(int i = INICIO; i <= FIM; i++){
        soma += i;
    }
    printf("%d\n", soma);
}
