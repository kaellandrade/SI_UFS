/*
CAP 2 EXER 14.
14. Faça um programa que receba o ano de nascimento de uma pessoa e o ano atual, calcule e mostre:
a) a idade dessa pessoa;
b) quantos anos ela terá em 2050.

*/
#include<stdlib.h>
#include<stdio.h>

int main(void){
    int ano_nascimento, ano_atual, idade, idade_prevista;
    #define PREVISAO 2100

    printf("Qual sua data de nascimento?\n");
    scanf("%d",&ano_nascimento);
    printf("Qual o ano atual?\n");
    scanf("%d",&ano_atual);

    idade = (ano_atual - ano_nascimento);
    idade_prevista = (PREVISAO - ano_nascimento);

    printf("IDADE:%d\nEm %d você terá %d anos\n",idade, PREVISAO, idade_prevista);
    
    return 0;
}