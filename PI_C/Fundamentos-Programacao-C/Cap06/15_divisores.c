#include<stdio.h>
#define LV 10
#define LVD 5

int VET[LV], VETD[LVD];
int flag = 0;

/*
    Faça um programa que preencha um primeiro vetor com dez números inteiros, e um segundos vetor
    com cinco números. O programa deverá mostrar um lista dos números do primeiro vetor com
    seus respectivos divisores armazenados no segundo vertor, bem como suas posições.
*/

int main(void){
    printf("**Valores para o primeiro vetor**\n");
    // Ler o vetor principal
    for (int i = 0; i < LV; i++){
        scanf("%d",&VET[i]);
    }

    printf("**Valores para o segundo vetor**\n");
    // Ler o segundo vetor
    for (int i = 0; i < LVD; i++){
        scanf("%d",&VETD[i]);
    }

    for (int i = 0; i < LV; i++){
        printf("\nNúmero %d\n",VET[i]);
        flag = 0;
        for (int j = 0; j < LVD; j++){
            if (VET[i]%VETD[j] == 0){
                printf("Divisível por %d na posição %d\n",VETD[j],j+1);
                flag = 1; // Há divisores
            }
                       
        }
        if (flag == 0){
                printf("Não há!\n");
            }
        
           
        printf("\n");
        
    }  
    
}
