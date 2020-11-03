#include <stdio.h>
#include <math.h>
#include <stdlib.h>

/*DESCRIÇÃO:
------------
A distância entre os pontos A e B é a medida do segmento que tem os dois pontos como extremidade. 
Por se tratar de dois pontos quaisquer, representaremos as coordenadas desses pontos de maneira genérica.

Nesse problema você irá desenvolver um programa que leia pares de pontos cartesianos e calcule 
as maiores distâncias encontradas e identifique em qual lugar do plano os pontos se encontram:

origem, eixo y positivo, eixo x positivo, eixo y negativo, eixo x negativo, quadrante 1,  quadrante 2,  quadrante 3 e  quadrante 4.




Formato de entrada:
Quantidade de pares de coordenadas
Sequência de pares de coordenadas


Formato de saída
Maior distância encontrada
Posição de cada par de coordenada no plano cartesiano

*/

float calcDistancia(int *Xa, int *Ya, int *Xb, int *Yb);
void teterminaLugar(int *Xa, int *Ya);

int main()
{
    float maiorDistancia;
    float distancia;
    int qtCordenada;
    scanf("%d", &qtCordenada);

    struct cordenadas
    {
        int Xa;
        int Ya;
        int Xb;
        int Yb;
    };
    struct cordenadas cordenada;      // Variável que irá conter um par de cordenada;
    struct cordenadas v[qtCordenada]; // Armazena todos os pares de cordenadas fornecidos.

    // Ler uma par de cordenada e, em seguida armazena no vetor v
    for (int i = 0; i < qtCordenada; i++)
    {
        scanf("%d %d %d %d", &cordenada.Xa, &cordenada.Ya, &cordenada.Xb, &cordenada.Yb);
        v[i] = cordenada;
    }

    // Determina a maior distância encontrada
    maiorDistancia = calcDistancia(&v[0].Xa, &v[0].Ya, &v[0].Xb, &v[0].Yb); // Considera a primera posição como a maior distância
    for (int i = 1; i < qtCordenada; i++)
    {
        distancia = calcDistancia(&v[i].Xa, &v[i].Ya, &v[i].Xb, &v[i].Yb);
        if (distancia > maiorDistancia)
        {
            maiorDistancia = distancia;
        }
    }

    // Percorre cada indice do vetor para determinar o quadrante do respectivo ponto;
    printf("%.2f\n", maiorDistancia);
    for (int i = 0; i < qtCordenada; i++)
    {
        teterminaLugar(&v[i].Xa, &v[i].Ya);
        teterminaLugar(&v[i].Xb, &v[i].Yb);
    }

    return EXIT_SUCCESS;
}

// Dada duas cordenadas (a,b) , (c, d) , calcDistancia calcula sua distância;
float calcDistancia(int *Xa, int *Ya, int *Xb, int *Yb)
{
    float distdb = sqrtf(pow((*Xb - *Xa), 2) + pow((*Yb - *Ya), 2));
    return distdb;
}

// Imprime o lugar no plano cartesiano de um determinado ponto (Xa, Ya);
void teterminaLugar(int *Xa, int *Ya)
{
    if (*Xa > 0 && *Ya > 0)
    {
        printf("quadrante 1");
    }
    else if ((*Xa < 0) && (*Ya > 0))
    {
        printf("quadrante 2");
    }
    else if (*Xa < 0 && *Ya < 0)
    {
        printf("quadrante 3");
    }
    else if ((*Xa > 0) && (*Ya < 0))
    {
        printf("quadrante 4");
    }
    else if (*Xa > 0 && *Ya == 0)
    {
        printf("eixo x positivo");
    }
    else if (*Ya > 0 && *Xa == 0)
    {
        printf("eixo y positivo");
    }
    else if (*Xa < 0 && *Ya == 0)
    {
        printf("eixo x negativo");
    }
    else if (*Ya < 0 && *Xa == 0)
    {
        printf("eixo y negativo");
    }
    else
    {
        printf("origem");
    }
    printf("\n");
}
