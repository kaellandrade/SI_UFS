#include<stdio.h>
#define LENGTH 5

/*
Faça um programa que preencha dois vetores com cinco elementos numéricos cada,
e depois, ordene-os de maneira crescente. Deverá ser gerado um terceiro vetor com dez posições,
composto pela junção dos elementos dos vetores anteriores, também, ordenado de maneira crescente.
*/

int vetX[LENGTH];
int vetY[LENGTH];
int resultado[LENGTH*2];
int auxiliar, j = 0;

int main(void){
    printf("-------Vetor X-------\n");
    for (int i = 0; i < LENGTH; i++)
    {
        scanf("%d",&vetX[i]);
    }
    
    printf("-------Vetor Y-------\n");
    for (int i = 0; i < LENGTH; i++)
    {
        scanf("%d",&vetY[i]);
    }

    // Ordena X
    for (int i = 0; i < LENGTH; i++){
        for (int j = 0; j < LENGTH-1; j++){
            if(vetX[j]>vetX[j+1]){
                auxiliar = vetX[j];
                vetX[j] = vetX[j+1];
                vetX[j+1] = auxiliar;
            }
        }
        
    }

    // Ordena Y
    for (int i = 0; i < LENGTH; i++){
        for (int j = 0; j < LENGTH-1; j++){
            if(vetY[j]>vetY[j+1]){
                auxiliar = vetY[j];
                vetY[j] = vetY[j+1];
                vetY[j+1] = auxiliar;
            }
        }
        
    }

    // Junta os vetores X Y ordenados;
    for (int i = 0; i < LENGTH; i++){
        resultado[j]=vetX[i];
        j++;
        resultado[j]=vetY[i];
        j++;

    }
    

    // Ordena os vetores X e Y juntados;
    for (int i = 0; i < LENGTH*2; i++){
        for (int j = 0; j < LENGTH*2-1; j++){
            if(resultado[j]>resultado[j+1]){
                auxiliar = resultado[j];
                resultado[j] = resultado[j+1];
                resultado[j+1] = auxiliar;
            }
        }
        
    }
    printf("---------------\n");
    // Mostra o resultado
    for (int i = 0; i < LENGTH*2; i++){
        printf("%d|", resultado[i]);
    }
    printf("\n");
    
}
