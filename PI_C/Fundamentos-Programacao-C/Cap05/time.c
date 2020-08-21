#include<stdio.h>
int main(void){
    #define TOTALTIMES 2
    #define TOTALJOGADORES 5

    int idade, menores_18, contakg;
    float altura, mediaidade,media_altura_todos, porcentagem, peso;

    menores_18 = 0;
    contakg = 0;
    media_altura_todos=0;

    for (int i = 1; i <= TOTALTIMES; i++){
        mediaidade =0;
        printf("Time %d---------------------\n",i);
        for (int j = 1; j <= TOTALJOGADORES; j++){
            printf("Jogador %d",j);
            printf("Sua idade\n");
            scanf("%d",&idade);
            printf("Sua altura\n");
            scanf("%f",&altura);
            printf("Digite seu peso\n");
            scanf("%f",&peso);

            mediaidade += idade;
            media_altura_todos += altura;
            if(idade<18){
                menores_18++;
            }
            if(peso > 80){
                contakg++;
            }
        }
        printf("Média idade do %dº time: %f\n",i,mediaidade/TOTALJOGADORES);
        
    }
    printf("Total menores 18 anos = %d\n",menores_18);
    printf("Média total alturas = %f\n",media_altura_todos/(TOTALJOGADORES*TOTALTIMES));
    printf("Porcentagem jogadores com mais de 80KG = %2.2f\n",(contakg*100.0)/(TOTALJOGADORES*TOTALTIMES));
}