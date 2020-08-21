#include<stdlib.h>
#include<stdio.h>
#include<locale.h>
/*
Um funcionário de uma empresa recebe, anualmente, aumento salarial. 
Sabe-se que:
A) Esse funcionário foi contratado em 2005, com salário inicial de 1.000,00.
B) Em 2006, ele recebeu aumento de 1,5% sobre seu salário inicial.
C) A partir de 2007 (inclusive), os aumentos salariais sempre corresponderam ao dobro do percentual do ano anterior.
Faça um programa que determine o salário atual desse funcionário.
*/

int main (void){

    setlocale(LC_ALL, "Portuguese");
    float salario = 1000;
    float aumento_inicial = 0.015;
    float new_sal = salario + (salario*aumento_inicial);
    int anoAtual;
    
    printf("Digite o ano atual:\n");
    scanf("%d",&anoAtual);
    for(int i = 2007; i <= anoAtual; i++){
        aumento_inicial *= 2;
        new_sal += new_sal*aumento_inicial;
        printf("Salário atual: R$ %.2f\n", new_sal);
        
    }
    return 0;
}
