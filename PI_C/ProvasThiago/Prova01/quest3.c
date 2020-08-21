#include<stdlib.h>
#include<stdio.h>

int main(void){
    int num;
    #define PARADA 200
    // Inicia minhas variáveis com os primeiros valores digitados;
    printf("Digite o 1º valor\n");
    scanf("%d", &num);
    int maior = num;
    int menor = num;

    for(int i = 2; i <= PARADA; i++){
        printf("Digite o %dº valor\n",i);
        scanf("%d", &num);
        // Verifica se é maior
        if(num >= maior){
            maior = num;
        }
        if(num <= menor){
            menor = num;
        }
    }
    printf("Maior : %d\nMenor: %d\n", maior, menor);
}