#include <stdio.h>
#include <math.h>
#include <stdlib.h>

#define TOTAL_ESFERAS 3
#define PI 3.1416

/*DESCRIÇÃO:
-----------
Escreva um programa que receba o raio de três esferas e forneça o volume das mesmas. 
A solução deve obrigatoriamente usar uma função chamada VolumeEsfera que receba o valor do raio como único parâmetro e retorne o valor do volume da esfera.
O seu programa deve chamar a função para calcular os volumes das esferas e de posse do valor imprimir o resultado. 
Portanto, a função não deve imprimir o valor.
Observação: O volume da esfera é calculado da seguinte forma: Volume= (4πR3)/3. Considere π como tendo o valor 3.1416.



Formato de entrada:
A entrada consiste de 3 linhas, sendo que em cada linha é fornecido o raio de uma das esferas (ponto flutuante).


Formato de saída:
A saída consiste de 3 linhas que correspondem às esferas cujos raios foram fornecidos na mesma ordem. 
Os valores são números reais (ponto flutuantes) com 2 casas decimais.

*/

double VolumeEsfera(double *r);

double main(){
    double v[TOTAL_ESFERAS];
    double r;

    // Ler os raios das esferas
    for (int i = 0; i < TOTAL_ESFERAS; i++){
        scanf("%lf", &r);
        v[i] = r;
    }
    // Calcula o o valor para cada raio armazenado em v
    for (int i = 0; i < TOTAL_ESFERAS; i++){
        printf("%.2lf\n", VolumeEsfera(&v[i]));
    }

    return EXIT_SUCCESS;
}

// Dado um raio r de uma esfera, VolumeEsfera calcula o volume da esfera
double VolumeEsfera(double *r){
    double volume;
    volume = (4*PI*powl(*r, 3.0))/3.0;
    return volume;
}