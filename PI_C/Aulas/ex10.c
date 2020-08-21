#include<stdlib.h>
#include<stdio.h>
/*
Faça um programa que preencha uma matriz M (2X2), calcule e mostre a matriz R, resultante
da multiplicação dos elementos de M pelo seu maior elemento.
*/
#define ROW 2 // Linhas
#define COL 2 // Colunas
int main(void){
    int M [ROW] [COL];
    int R [ROW] [COL];

    int maior;
    // grava valores em M
    for(int linha = 0; linha<ROW;linha++){
        for(int coluna = 0; coluna < COL; coluna++){
            printf("%d Linha, %d Coluna: ", linha+1, coluna+1);
            scanf("%d", &M[linha] [coluna]); // Armazena o valor na matriz.
            // Captura o maior valor digitado.
            int valor = M[linha] [coluna];
            if(valor >= maior){
                maior = valor;
            }
        }
    }
    // Grava valores em R basedos em M
    for(int linha = 0; linha < ROW; linha++){
        for (int coluna = 0; coluna < COL; coluna++){
            R[linha] [coluna] = M[linha] [coluna] * maior;
        }
    }
    // printf("Matriz R = M * %d", maior);
    // Mostra valor de R
    for (int linha = 0; linha < ROW; linha++){
        for (int coluna = 0; coluna < COL; coluna++){
            printf("|%.2d| ",R[linha] [coluna]);
        }
        printf("\n");
        
    }
    
    return 0;
}