#include <stdio.h>
#include <math.h>
#include <stdlib.h>
/*DESCRIÇÃO:
------------
Na última aula de matemática, Rafael, Beto e Carlos aprenderam algumas novas funções matemáticas. 
Cada um deles se identificou com uma função em especial, e resolveram competir para ver quem tinha a função de maior resultado.
A função que Rafael escolheu é r(x, y) = (3x)² + y².
Já Beto escolheu a função b(x, y) = 2(x²) + (5y)².
Carlos, por sua vez, escolheu a função c(x, y) = -100x + y³.
Dados os valores x e y, diga quem escolheu a função com o maior resultado.
Observação: É obrigatório definir e utilizar as funções r, b e c, conforme especificado acima

Formato de entrada:
A primeira linha de entrada contém um inteiro N que determina a quantidade de casos de teste. Cada caso de teste consiste em dois inteiros x e y(1 ≤ x, y ≤ 100), indicando as variáveis a serem passadas como parâmetros para as funções.

Formato de saída:
Para cada caso de teste imprima uma linha, contendo uma frase, indicando quem ganhou a competição. 
Por exemplo, se Rafael ganhar a competição, imprima “Rafael ganhou”. Assuma que nunca haverá empates.
*/

int r(int *x, int *y);
int b(int *x, int *y);
int c(int *x, int *y);
void imprimeCamp(int *rafael, int *beto, int *carlos);
void repImprimir(int *p);

int main(){
    int inputs;
    scanf("%d", &inputs);
    repImprimir(&inputs);
    return 0;
}

// Função do rafael
int r(int *x, int *y){
    return pow(3* (*x), 2) + pow(*y, 2);
}

// Função do beto
int b(int *x, int *y){
    return 2 * pow(*x, 2) + pow(5 * (*y), 2);
}

// Função do carlos
int c(int *x, int *y)
{
    return  pow(*y, 3) - 100 * (*x);
}

void imprimeCamp(int *r, int *b, int *c){
    if (*r > *b && *b > *c)
    {
        printf("Rafael ganhou\n");
    }
    else if (*b > *c)
    {
        printf("Beto ganhou\n");
    }
    else
    {
        printf("Carlos ganhou\n");
    }
}

void repImprimir(int *p){
    while (*p > 0){
        int x;
        int y;

        scanf("%d%d", &x, &y);

        int rafael = r(&x, &y);
        int beto = b(&x, &y);
        int carlos = c(&x, &y);
        imprimeCamp(&rafael, &beto, &carlos);

        (*p)--;
    }
}