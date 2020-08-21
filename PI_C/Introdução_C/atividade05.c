/*
Fatorial
 */
#include<stdlib.h>
#include<stdio.h>

int number;
int fat = 1;

int main(void){
    printf("Digite um número para calcular a fatorial:\n");
    scanf("%d",&number);
    for(int i = 1; i <= number; i++){
        fat *= i;
    }
    printf("%d\n",fat);
}