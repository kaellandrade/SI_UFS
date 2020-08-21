/*
Faça um programa que receba três números obrigatoriamente em ordem crescente e um quarto núme-
ro que não siga essa regra. Mostre, em seguida, os quatro números em ordem decrescente. Suponha
que o usuário digitará quatro números diferentes.
*/
#include<stdlib.h>
#include<stdio.h>

int main(void){
    int number1, number2, number3, number4;
    printf("Digite 3 números em ordem crescente: \n");
    scanf("%d %d %d",&number1,&number2,&number3);
    printf("Digite um quarto número (sem seguir a ordem): \n");
    scanf("%d",&number4);

    if(number4 >= number3){
        printf("%d %d %d %d", number4, number3, number2, number1);

    } else if(number4 >= number2 && number4 <= number3){
        printf("%d %d %d %d", number3, number4, number2, number1);
    }else if(number4 >= number1 && number4 <= number2){
        printf("%d %d %d %d", number3, number2, number4, number1);

    } else{
        printf("%d %d %d %d", number3, number2, number1, number4);
        
    }
    printf("\n");

    return 0;
}