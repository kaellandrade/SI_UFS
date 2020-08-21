#include<stdlib.h>
#include<stdio.h>

int calculaFAT(int num){
    int fat = 1;
    for (int i = 1; i <= num; i++)
    {
        fat *= i;
    }
    return fat;       
}

int main(void){
    #define LENGTH 5
    int VETOR [LENGTH];
    int VETORFAT [LENGTH];
    // Armazena os meus valores em VETOR e as fatoriais em VETORFAT;
    for ( int i = 0; i < LENGTH; i++)
    {
        printf("Digite o %d º valor: ", i+1);
        scanf("%d", &VETOR[i]);
        VETORFAT[i] = calculaFAT(VETOR[i]); // Calcula a fatorial separadamente.
    } 

    // Mostra os valores de VETORFAT
    for (int i = 0; i < LENGTH; i++)
    {
        printf("%d\n",VETORFAT[i]);
    }
    
}