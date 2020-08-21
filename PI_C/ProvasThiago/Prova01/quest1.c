#include<stdlib.h>
#include<stdio.h>

int main(void){
    float salario, percentual;
    printf("Digite o salário atual e o percentual de aumento repectivamente\n");
    scanf("%f %f",&salario,&percentual);
    printf("Seu novo salário será: %2.2f\n", salario+(salario*percentual));
}