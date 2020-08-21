#include<stdio.h>
#include<math.h>
/*
5. Faça um programa que receba um número positivo e maior que zero, calcule e mostre:
A) O número digitado ao quadrado;
B) O número digitado ao cubo;
C) A raiz quadrada do número digitado;
D) A raiz cúbica do número digitado;
*/

int main()
{
    float num, quadrado, cubo, raiz, raizcub;

    printf("Digite um número?\n");
    scanf("%f", &num);
    quadrado = pow(num,2);

    cubo = pow(num, 3);
    raiz = pow(num, 0.5);
    raizcub = pow(num, 0.33);
    printf("%2.2f² = %2.2f\n", num, quadrado);
    printf("%.2f³ = %.2f\n",  num, cubo);
    printf("√%2.2f = %2.2f\n", num, raiz);
    printf("∛%2.2f = %2.2f\n", num, raizcub);

    return 0;
}
