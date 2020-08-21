/*
Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito.
Foram obtidos os seguintes dados:
a) código da cidade;
b) número de veículos de passeio;
c) número de acidentes de trânsito com vítimas.

Deseja-se saber:
a) qual é o maior e qual é o menor índice de acidentes de trânsito e a que cidades pertencem;
b) qual é a média de veículos nas cinco cidades juntas;
c) qual é a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.

*/
#include<stdio.h>
#include<stdlib.h>

// int calcula_fat(int num){
    
// }

int main(void){
    #define CIDADES 2
    int codigo_cidade, veiculos_passeio, acidentes;

    int maior_indice_acidentes, menor_indice_acidentes, soma_veiculos, soma_acidentes, conta_cidade;
    float media_veiculos, media_acidentes;
    int codigo_menor_indice, codigo_maior_indice;

    soma_veiculos = 0;
    soma_acidentes = 0;
    conta_cidade = 0;


    for (int i = 1; i <= CIDADES; i++){
        printf("%dº Cidade: \n",i);
        printf("Código: \n");
        scanf("%d", &codigo_cidade);
        printf("Número veículos de passeio: \n");
        scanf("%d", &veiculos_passeio);
        printf("Número de acidentes de trânsito com vítimas: \n");
        scanf("%d", &acidentes);
        if(i==1){
            maior_indice_acidentes = acidentes;
            menor_indice_acidentes = acidentes;
            codigo_menor_indice = codigo_cidade;
            codigo_maior_indice = codigo_cidade;
        }

        soma_veiculos += veiculos_passeio;
    
        if (acidentes > maior_indice_acidentes){
            maior_indice_acidentes = acidentes;
            codigo_maior_indice = codigo_cidade;
        } else if(acidentes < maior_indice_acidentes){
            menor_indice_acidentes = acidentes;
            codigo_menor_indice = codigo_cidade;
        }

        if(veiculos_passeio < 2000){
            soma_acidentes += acidentes;
            conta_cidade++;
        } 
    }
    media_veiculos = soma_veiculos/CIDADES;
    media_acidentes = soma_acidentes/conta_cidade;
    printf("----------------------------------------------------------\n");
    printf("Maior índice de acidentes: %d\nCidade: %d\n",maior_indice_acidentes, codigo_maior_indice);
    printf("Menor índice de acidentes: %d\nCidade: %d\n",menor_indice_acidentes, codigo_menor_indice);
    printf("Média de veículos das %d cidades: %.2f\n", CIDADES, media_veiculos);
    // printf("Média de acidentes em %d cidades de menos 2.000 veículos: %.2f\n", CIDADES, media_acidentes); ERRO AQUI!

}