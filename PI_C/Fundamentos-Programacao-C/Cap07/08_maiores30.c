#include<stdio.h>
#define L 3
#define C 3

int MAT1[L][C];
int MAT2[L][C];
int qtmaior = 0;


/*
Elabore um programa que preencha uma matriz 6 X 4 com números inteiros, calcule e mostre quantos
elementos dessa matriz são maiores que 30 e, em seguida, monte uma segunda matriz com os elemen-
tos diferentes de 30. No lugar do número 30, da segunda matriz, coloque o número zero.
*/
int main(void){
    printf("----Digite a matriz [%dX%d]----\n",L,C);
    for (int i = 0; i < L; i++)
    {
        for (int j = 0; j < C; j++)
        {
            scanf("%d",&MAT1[i][j]);
            if(MAT1[i][j] > 30){
                qtmaior++;
            }
        }
        
    }

    // Add 0 se for 30
    for (int i = 0; i < L; i++)
    {
        for (int j = 0; j < C; j++)
        {
            if(MAT1[i][j] != 30){
                MAT2[i][j] = MAT1[i][j];
            }else{
                MAT2[i][j] = 0;
            }
        }
        
    }
    printf("\n=+=+=+=+=\n");
    // Mostra a matriz final
    for (int i = 0; i < L; i++)
    {
        for (int j = 0; j < C; j++)
        {
            printf("%.2d|",MAT2[i][j]);
        }
        printf("\n");   
    }
    printf("Maiores que 30:%d\n",qtmaior);
}
