#include<stdlib.h>
#include<stdio.h>
/*
Faça um programa que leia um valor N inteiro e positivo. Calcule e mostre o valor de E,
conforme a fórmula a seguir:
    E = 1 + 1/1! + 1/2! + 1/3! ... + 1/N!
*/

int main (void){
    int n;
    float e = 1.0;
    int fat;

    printf("Digite um valor inteiro: \n");
    scanf("%d",&n);

    for(int i = 1; i <= n; i++){
        fat = 1;
        for (int j = 1; j <= i; j++){
            fat *= j;
        }
        e += (1/fat);
    }
    printf("E = %.2f\n", e);
}