#include<stdio.h>
#define MAX_VEL 50

float CalculaMulta(float vel){
    float multa = 0.0;
    if(vel > 50){

        if(vel > 50 && vel <= MAX_VEL*10/100 + MAX_VEL){
            multa = 230;
        }else if(vel > 55 && vel <= MAX_VEL*20/100 + MAX_VEL){
            multa = 340;
        }else{
            multa = (vel - MAX_VEL) * 19.28;
        }
        
    }
    return multa;
}

int main(){ 
    float vel;
    scanf("%f", &vel);
    printf("%.2f\n", CalculaMulta(vel));
    return 0;
}
