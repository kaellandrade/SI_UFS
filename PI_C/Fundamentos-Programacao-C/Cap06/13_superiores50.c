#include<stdio.h>
#define LENGTH 10
int Flag = 0;
int VET [LENGTH];

/*
    Faça um programa que preencha um vetor com dez números inteiros, calcule e mostre
    os números superiores a cinquenta e suas respectivas posições. O programa deverá
    mostrar mensagem se não existir nenhum número nessa condição.
*/

int main(void){
    // Ler o vetor
    for(int i = 0; i < LENGTH; i++){
        printf("%dº valor:\n",i+1);
        scanf("%d",&VET[i]);
        if (VET[i] > 50){
            Flag = 1; // Indica que há maiores que 50;
        }
        
    }

    if(Flag){// Se houver maiores que 50, iremos percorrer o vetor para encontrá-los.
        for (int i = 0; i < LENGTH; i++)
        {
            if (VET[i]>50){
                printf("Número: %d --- Posição: %d\n",VET[i],i+1);
            }
        }
        
    }else{ // Caso não haja maiores que 50;
        printf("Não há números maiores que 50.\n");
    }
}