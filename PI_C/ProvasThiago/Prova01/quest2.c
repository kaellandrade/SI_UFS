#include<stdlib.h>
#include<stdio.h>

int main(void){
    int hora_inicio, mim_inicio, hora_fim, mim_fim;
    int duracao_hora, duracao_min;

    // Inicio
    printf("Hora inicial do jogo\n");
    scanf("%d", &hora_inicio);
    printf("Minutos inicial do jogo\n");
    scanf("%d", &mim_inicio);

    // Fim
    printf("Hora final do jogo\n");
    scanf("%d", &hora_fim);
    printf("Minutos finais do jogo\n");
    scanf("%d", &mim_fim);

    // Calculando
    if(hora_inicio > hora_fim){ // Começou em um dia e terminou no outro.
        duracao_hora =  (24 - hora_inicio) + hora_fim;
    } else{
        duracao_hora = abs(hora_inicio - hora_fim);
    }
    duracao_min = mim_fim - mim_inicio;

    printf("Duração do jogo: %.2d H: %.2d\n", duracao_hora, duracao_min);
}