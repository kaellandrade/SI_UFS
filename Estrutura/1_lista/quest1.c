#include<stdio.h>
#include<math.h>

// Dada duas cordenadas (a,b) , (c, d) , calcDistancia calcula sua distânca;
float calcDistancia(int Xa, int Ya, int Xb, int Yb){
    float distdb = sqrtf( pow((Xb - Xa), 2)  + pow((Yb - Ya), 2));
    return distdb;
}

// Imprime o lugar de um determinado ponto (Xa, Ya);
void teterminaLugar(int Xa, int Ya){
    if(Xa > 0 && Ya > 0){
        printf("quadrante 1");
    }else if((Xa < 0) && (Ya > 0)){
        printf("quadrante 2");
    }else if(Xa < 0 && Ya < 0){
        printf("quadrante 3");
    }else if((Xa > 0) && (Ya < 0)){
        printf("quadrante 4");
    }else if(Xa > 0 && Ya == 0){
        printf("eixo x positivo");
    }else if(Ya > 0 && Xa == 0){
        printf("eixo y positivo");
    }else if(Xa < 0 && Ya == 0){
        printf("eixo x negativo");
    }else if(Ya < 0 && Xa == 0){
        printf("eixo y negativo");
    }else{
        printf("origem");
    }
    printf("\n");
}


int main(){
    printf("%.2f \n", calcDistancia(100, 210, 40, 1));
    teterminaLugar(1, 0);
    return 0;
}
