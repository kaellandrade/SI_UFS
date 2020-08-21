#include<stdio.h>
#include<stdlib.h>
#include<math.h>
int main(void)
{
    #define PI 3.14159265359

    float lado,raio,area;
    printf("Qual o lado do quadrado?\n");
    scanf("%f",&lado);
    raio = lado/2.0;
    area = PI * pow(raio,2.0);
    printf("Área do círculo:%f\n",area);
    return 0;
}
