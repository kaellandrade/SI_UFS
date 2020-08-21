/*
CAP 2 EXER 13.
Sabe-se que:
pé = 12 polegadas
1 jarda = 3 pés
1 milha = 1,760 jarda
Faça um programa que receba uma medida em pés, faça as conversões a seguir e mostre os resultados.
a) polegadas;
b) jardas;
c) milhas.
*/
#include<stdlib.h>
#include<stdio.h>

int main(void){
    float pes, polegadas, jardas, milhas;

    printf("Digite a medida em Pés:\n");
    scanf("%f",&pes);
    polegadas = pes*12;
    jardas = pes/3;
    milhas = jardas/1760;
    printf("POLEGAS: %.2f\nJARDAS: %.2f\nMILHAS: %.4f\n",polegadas, jardas, milhas);
    
    return 0;
}