/*
CAP 2 EXER 15. 
O custo ao consumidor de um carro novo é a soma do preço de fábrica com o percentual de lucro do
distribuidor e dos impostos aplicados ao preço de fábrica. Faça um programa que receba o preço de fá-
brica de um veículo, o percentual de lucro do distribuidor e o percentual de impostos, calcule e mostre:
a) o valor correspondente ao lucro do distribuidor;
b) o valor correspondente aos impostos;
c) o preço final do veículo.


*/
#include<stdlib.h>
#include<stdio.h>

int main(void){
    float preco_fabrica, percentual_lucro, percentual_imposto,lucro_distribuidor, valor_imposto, preco_final;
    

    printf("Digite, Preço de fábrica, Percentual lucro, Percentual imposto. Respectivamente.\n");
    scanf("%f %f %f",&preco_fabrica, &percentual_lucro, &percentual_imposto);

    lucro_distribuidor = preco_fabrica * (percentual_lucro/100);
    valor_imposto = preco_fabrica * (percentual_imposto/100);
    preco_final = preco_fabrica + lucro_distribuidor + valor_imposto;

    printf("LUCRO FABRICANTE: %.2f\nVALOR IMPOSTO: %.2f\nPREÇO FINAL: %.2f\n",lucro_distribuidor, valor_imposto, preco_final);
    
    return 0;
}