/*
CAP 2 EXER 16.

Faça um programa que receba o número de horas trabalhadas e o valor do salário mínimo, calcule e
mostre o salário a receber, seguindo estas regras:

a) a hora trabalhada vale a metade do salário mínimo.
b) o salário bruto equivale ao número de horas trabalhadas multiplicado pelo valor da hora trabalhada.
c) o imposto equivale a 3% do salário bruto.
d) o salário a receber equivale ao salário bruto menos o imposto.



*/
#include<stdlib.h>
#include<stdio.h>

int main(void){
    float valor_sal_minimo, valor_sal_receber, sal_bruto, imposto; 
    float horas_trabalhadas, hora_trabalhada;
    

    printf("Qual o número de horas trabalhadas:\n");
    scanf("%f", &horas_trabalhadas);

    printf("Qual o valor do salário mínimo R$: \n");
    scanf("%f",& valor_sal_minimo);
    hora_trabalhada = (valor_sal_minimo/2.0);
    sal_bruto = horas_trabalhadas * hora_trabalhada;
    imposto = sal_bruto * (3.0/100.0);

    valor_sal_receber = sal_bruto - imposto;

    printf("A receber: %.2f R$\n", valor_sal_receber);
    
    return 0;
}