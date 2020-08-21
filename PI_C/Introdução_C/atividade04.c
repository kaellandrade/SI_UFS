/*
Calculadora
 */
#include<stdlib.h>
#include<stdio.h>

float numA, numB;
int resposta, intervalo;

int main(void){
    printf("Valor de A\n");
    scanf("%f",&numA);
    printf("Valor de B\n");
    scanf("%f",&numB);
    printf("Qual a operação 1 (+) 2 (-) 3 (*) 4 (/) ?\n");
    do
    {
        scanf("%d",&resposta);
        intervalo = (resposta >= 1 && resposta <= 4);        
    } while (!intervalo);

    if (resposta==1){
        printf("%f\n",numA+numB);

    }else if(resposta == 2){
        printf("%f\n", numA - numB);

    }else if (resposta == 3){
        printf("%f\n",numA*numB);

    }else{
        printf("%f\n",numA/numB);
    }
    
}
