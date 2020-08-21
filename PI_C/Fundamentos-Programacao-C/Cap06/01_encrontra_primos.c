#include<stdio.h>
#define LENGTH 9
int vetor[LENGTH];

/*
Faça um programa que preencha um vetor com nove números inteiros, calcule e mostre os números primos
e suas respectivas posições
*/



// Função que calcula se o número é primo.
int ePrimo(int num){
    int conta_divisores = 0;
    for(int i = 1; i<= num; i++){
        if(num % i == 0 ){
            conta_divisores++;
        }
    }
    if(conta_divisores == 2){
        return 1;
    }else{
        return 0;
    }
}

int main(){
    // Preenche o vetor;
    for(int i = 0; i < LENGTH;i++){
        printf("Digite o %dº número: \n",i);
        scanf("%d",&vetor[i]);
    }
    // Mostra os primos e suas respecticas posições;
    for(int i = 0; i < LENGTH; i++){
        if (ePrimo(vetor[i])){
            printf("%d é primo sua posição é: %d\n",vetor[i],i);
        }
        
    }
}
