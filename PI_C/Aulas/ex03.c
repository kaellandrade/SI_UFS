#include<stdio.h>
/*
5. Faça um programa que receba o salário de um funcionário e o
percentual de aumento, calcule e mostre o valor do aumento e o novo sálario.
*/

int main()
{
    float salario, percentualaumento, aumento;
    printf("Qual o seu salário?\n");
    scanf("%f", &salario);
    printf("Qual foi seu percentual de aumento? Ex(0.25)\n");
    scanf("%f",&percentualaumento);
    aumento = salario * percentualaumento;
    printf("Seu aumento será de %4.2f R$\n", aumento);
    printf("Seu novo salário será de %4.2f R$\n", salario + aumento);
    return 0;
}
