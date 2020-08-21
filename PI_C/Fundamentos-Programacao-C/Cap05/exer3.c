/*
Faça um programa que leia um número N que indica quantos valores inteiros e positivos devem ser
lidos a seguir. Para cada número lido, mostre uma tabela contendo o valor lido e o fatorial desse valor.
*/
#include<stdio.h>
#include<stdlib.h>

int calcula_fat(int num){
    int fat = 1;
    for(int i = 1; i <= num; i++){
        fat *= i;
    }
    return fat;
}

int main(void){
    int total;
    int valor;
    printf("Deseja ler quantos valores? \n");
    scanf("%d",&total);
    for(int i = 1; i <= total; i++){
        printf("Digite o %dº valor\n",i);
        scanf("%d",&valor);
        printf("%d! =  %d\n", valor, calcula_fat(valor));
    }
}