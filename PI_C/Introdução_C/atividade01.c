/*
Escreva um programa que imprima todos os números pares entre 2 e 50.
 */
#include<stdlib.h>
#include<stdio.h>

#define INICIO 2
#define FIM 50

int main(void){
    for(int i = INICIO; i <= FIM; i++){
        if (i%2 == 0){
            printf("%d, ",i);
        }
    }
    printf("\n");
}
