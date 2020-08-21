#include<stdio.h>
#define LINHAS 2
#define COLUNAS 2
int MATRIZ[LINHAS][COLUNAS];
int indice_linha,indice_coluna, menor_elemento_matriz,  maior;
/*
    Na teoria dos sistemas, define-se o elemento MINMAX de uma matriz como o maior elemento da linha
    em que se encontra o menor elemento da mariz. Elabore um programa que carregue uma matriz
    4 X 7 com números reais, calcule e mostre seu MINMAX e sua posição (linha e coluna).
*/

int main(void){
    // Lendo a matriz;
    for (int i = 0; i < LINHAS; i++){
        for (int j = 0; j < COLUNAS; j++){
            scanf("%d",&MATRIZ[i][j]);
        }
        
    }

    // Procurando o indice da linha que contém o menor elemento;
    menor_elemento_matriz = MATRIZ[0][0];
    indice_linha = 0;
    for (int i = 0; i < LINHAS; i++){
        for (int j = 0; j < COLUNAS; j++){
            if (MATRIZ[i][j]<menor_elemento_matriz)
            {
                menor_elemento_matriz = MATRIZ[i][j];
                indice_linha = i;
            }
            
        }
        
    }

    // Encontra o MINMAX
    maior = MATRIZ[indice_linha][0];
    indice_coluna = 0;
    for (int j = 0; j < COLUNAS; j++){
        if (MATRIZ[indice_linha][j] > maior)
        {
            maior = MATRIZ[indice_linha][j];
            indice_coluna = j;
        }
        
    }
    printf("MINMAX: %d LINHA:%d COLUNA: %d\n",maior, indice_linha+1, indice_coluna+1);
    

}