#include<stdio.h>
#include<stdlib.h>

int main(void){
    int idade;
    float peso;
    // Menores de 20 anos.
    printf("Qual a sua idade?\n");
    scanf("%d",&idade);

    printf("Qual o seu peso?\n");
    scanf("%f",&peso);

    if(idade < 20){
        if(peso <= 60.0){
            printf("Risco 9\n");
        }
        else if (peso > 60.0 && peso < 90.0){
            printf("Risco 8\n");
        }else{
            printf("Risco 7\n");
        }
    }

    // Entre 20 anos e 50 anos;
    else if(idade >=20 && idade <50){

        if(peso <= 60.0){
            printf("Risco 6\n");
        }
        else if(peso > 60.0 && peso < 90.0){
            printf("Risco 5\n");
        } else{
            printf("Risco 4\n");
        }
    }
    // Maiores de 50 anos.
    else{
        if(peso <= 60.0){
            printf("Risco 3\n");
        }
        else if (peso > 60.0 && peso < 90.0){
            printf("Risco 2\n");
        }
        else{
            printf("Risco 1\n");
        }
    }
}