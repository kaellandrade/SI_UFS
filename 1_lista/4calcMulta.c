#include<stdio.h>
#include<stdlib.h>

#define MAX_VEL 50
/*DESCRIÇÃO:
------------
Devido ao grande número de acidentes ocorridos recentemente na rua principal da cidade, um sistema de radares será instalado para multar os condutores que excederem os 50 km/h permitidos. 
Aqueles que excederem a velocidade, mas estiverem no máximo 10% acima da velocidade limite serão multados em R$ 230. 
Já os condutores que excederem a velocidade permitida em até 20% serão multados em R$ 340. 
Caso a velocidade do motorista exceda o limite em mais de 20%, ele terá que pagar uma multa de R$ 19,28 por cada km excedido.
Escreva uma função chamada CalculaMulta que receba como entrada a velocidade de um condutor e retorne o valor da multa que ele terá que pagar.



Formato de entrada:
Um valor inteiro

Formato de saída:
Um valor real

*/
float CalculaMulta(float *p_vel);
int main(){ 
    float vel;
    scanf("%f", &vel);
    printf("%.2f\n", CalculaMulta(&vel));
    return EXIT_SUCCESS;
}

float CalculaMulta(float *p_vel){
    float multa = 0.0;
    if(*p_vel > 50){

        if(*p_vel > 50 && *p_vel <= MAX_VEL*10/100 + MAX_VEL){
            multa = 230;
        }else if(*p_vel > 55 && *p_vel <= MAX_VEL*20/100 + MAX_VEL){
            multa = 340;
        }else{
            multa = (*p_vel - MAX_VEL) * 19.28;
        }
        
    }
    return multa;
}