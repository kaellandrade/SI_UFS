#include <stdio.h>
#include <math.h>
/**
Ler quatro valores correspodentes aos eixos x e y dois pontos
quaisquer no plano, p1(x1, y1) e p2(x2,y2) e calcule a distância
entre eles;
*/

float calcPoints(float x1, float y1, float x2, float y2);

int main()
{
    float x1, x2, y1, y2;
    printf("Digite o primeiro e o segundo ponto (x,y)\n");
    scanf("%f %f %f %f", &x1, &y1, &x2, &y2);

    printf("Ditância ente (%.2f, %.2f) e (%.2f, %.2f): %.2f\n",
           x1, y1, x2, y2, calcPoints(x1, y1, x2, y2));
    return 0;
}

float calcPoints(float x1, float y1, float x2, float y2)
{
    return sqrt(powf((x2 - x1), 2) + powf((y2 - y1), 2));
}