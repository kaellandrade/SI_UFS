/*
Tabuada de 0X10
 */
#include<stdlib.h>
#include<stdio.h>

#define INICIO 0
#define FIM 10
int number ;

int main(void){
    printf("Digite um número para ver a sua tabuada\n");
    scanf("%d", &number);
   
    
    for(int i = INICIO; i <= FIM; i++){
        printf("%d * %d = %d\n", number, i, number * i);
    }
    printf("\n");
}
