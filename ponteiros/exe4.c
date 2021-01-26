#include <stdio.h>
#include <stdlib.h>

// Protótipo da função;
void modificaVetsqn(int x);
void imprimeVet(int *p);

int main(){
    int vet[] = {1, 2, 3, 4, 5, 0};
    // int *pTeste = &teste;

    imprimeVet(&vet[0]);
    printf("\n");

    return 0;
}

void modificaVetsqn(int x){
    x = 40;
}
void imprimeVet(int *p){
    for (int i = 0; i < 6; i++){
        printf("%d", p[i]);
    }
    
}