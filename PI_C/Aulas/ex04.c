#include<stdio.h>
/*
5. Faça um programa que receba o salário base de um funcionário, calcule e mostre a receber,
sabendo-se que o funcionário tem gratificação de 5% sobre o salário base
e paga imposto de 7% também sobre o salário base.
*/

int main()
{
    float salariobase,areceber, gratificacao, imposto;
    printf("Qual o seu salário base?\n");
    scanf("%f", &salariobase);
    gratificacao = salariobase * 0.05;
    imposto = salariobase * 0.07;
    areceber = salariobase + gratificacao - imposto;
    printf("Você irá receber: %4.2f R$\n", areceber);
    return 0;
}
