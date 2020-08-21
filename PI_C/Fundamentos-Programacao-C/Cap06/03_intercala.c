#include<stdio.h>
#define LENGTH 3
/*
Faça um programa que preencha dois vetores de dez elementos numéricos cada um e mostre o vetor
resultante da intercalação deles.
*/
int vetor1[LENGTH];
int vetor2[LENGTH];
int vetor3[LENGTH*2];
int j=0;

int main(){
    printf("---------Primeiro vetor---------\n");
    for (int i = 0; i < LENGTH; i++)
    {
        printf("Digite o º%d valor para vetor1:\n",i+1);
        scanf("%d", &vetor1[i]);

    }
    printf("---------Segundo vetor---------\n");
    for (int i = 0; i < LENGTH; i++)
    {
        printf("Digite o º%d valor para vetor2:\n",i+1);
        scanf("%d", &vetor2[i]);

    }

    for ( int i = 0; i < LENGTH; i++){
        vetor3[j]=vetor1[i];
        j++;
        vetor3[j] = vetor2[i];
        j++;
    }
    

    
    // Mostra a intercalação
    for (int i = 0; i < LENGTH*2; i++)
    {
        printf("%d|",vetor3[i]);
    }
    printf("\n");
    
    
    return 0;
}
