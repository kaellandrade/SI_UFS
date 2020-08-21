#include<stdio.h>
#define LENGTH 12 
/*
Faça um programa que receba a temperatura média de cada mês
do ano. Calcule e mostre a maior e a menor temperatura e em que mês
o correram.
*/
float TEMP[LENGTH], menor, maior, indice_maior, indice_menor;

int mes(int indice){
    if (indice == 0)
    {
        printf("Janeiro.\n");
    }else if(indice == 1){
        printf("Fevereiro.\n");
    }else if(indice == 2){
        printf("Março.\n");
    }
    else if(indice == 3){
        printf("Abril.\n");
    }else if(indice == 4){
        printf("Maio.\n");
    }else if(indice == 5){
        printf("Junho.\n");
    }else if(indice == 6){
        printf("Julho.\n");
    }else if(indice == 7){
        printf("Agosto.\n");
    }else if(indice == 8){
        printf("Setembro.\n");
    }else if(indice == 9){
        printf("Outubro.\n");
    }else if(indice == 10){
        printf("Novembro.\n");
    }else{
        printf("Dezembro.\n");
    }
    
}


int main(void){
    for (int i = 0; i < LENGTH; i++){
        printf("%dº mês: \n",i+1);
        scanf("%f",&TEMP[i]);
        if(i == 0){ // A primeira temperatura é a maior e menor.
            menor = TEMP[i]; 
            maior = TEMP[i];
        }else{ // Caso não seja o primeiro valor digitado.
            if(TEMP[i] > maior){
                maior = TEMP[i]; 
                indice_maior=i;
            }
            if(TEMP[i] < menor){
                menor = TEMP[i];
                indice_menor =i;
            }
        }
    }
    printf("Maior temperatura: %.2f, ",maior);
    mes(indice_maior);
    printf("\n----------------\n");
    printf("Menor temperatura: %.2f, ",menor);
    mes(indice_menor);
}