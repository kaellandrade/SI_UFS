#include <stdio.h>
#include <math.h>
#define TOTAL_ESFERAS 3

// Dado um raio r de uma esfera, VolumeEsfera calcula o volume da esfera
double VolumeEsfera(double r){
    double volume;
    volume = (4*3.1416*powl(r, 3.0))/3.0;
    return volume;
}

double main(){
    double v[TOTAL_ESFERAS];
    double r;

    for (int i = 0; i < TOTAL_ESFERAS; i++){
        scanf("%lf", &r);
        v[i] = r;
    }

    for (int i = 0; i < TOTAL_ESFERAS; i++){
        printf("%.2lf\n", VolumeEsfera(v[i]));
    }

    return 0;
}