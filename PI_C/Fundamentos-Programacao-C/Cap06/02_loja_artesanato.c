#include<stdio.h>
#define LENGTH 2

float vetor_precos[LENGTH];
int vetor_quantidades[LENGTH];
int quantidade_vendida, valor_unitario, indice;
float valor_total, valor_geral, comissao, maior;


/*
Uma pequena loja de artesanato possui apenas um vendedor e comercializa dez tipos de objetos. O vendedor
recebe, mensalmente, salário de R$ 545,00, acrescido de 5% do valor total de suas vendas.
O valor uitário dos objetos deve ser informado e armazenado em uma vetor; a quantidade vendidida
de cada peça deve ficar em outro vetor, mas na mesma posição. Crie um programa que receba os preços
e as quantidades vendidas, armazenando-os em seus respecticos vetores (ambos com tamanho dez).

Depois, determine e mostre:
Um relatório contendo: quantidade vendida, valor unitário, e valor total de cada objeto. 
Ao final, deverão se mostrados o valor geral das vendas e o valor da comissão que será paga ao vendedor; e
o valor do objeto mais vendido e sua posição no vetor(não se preocupe com empates).
*/

// Ler os preços e a quantidade.
int LerPrecosQuantidades(){
    for(int i = 0; i < LENGTH; i++){
        printf("Digite o preço para o %dº produto:\n",i+1);
        scanf("%f",&vetor_precos[i]);

        printf("Digite a quantidade vendida do produto: \n");
        scanf("%d",&vetor_quantidades[i]);
    }
}


int Relatorio(){
    valor_geral = 0;
    indice = 0;
    maior = vetor_quantidades[0];
    // Encontra o mais vendido
    for (int i = 0; i < LENGTH; i++){
        if (vetor_quantidades[i]>maior)
        {
            maior = vetor_quantidades[i];
            indice = i;

        }
        
    }


    //Calcula a quantidade vendida valor e o total de todos os produtos
    printf("Quantidade...........Valor..........Total\n");
    for (int i = 0; i < LENGTH; i++){
        valor_total= vetor_precos[i]*vetor_quantidades[i];
        printf("%d...................R$%2.2f..........R$%2.2f\n",vetor_quantidades[i],vetor_precos[i],valor_total);
        valor_geral += valor_total;
    }
    comissao=valor_geral*(5.0/100.0);


    printf("Valor geral das vendas: R$%2.2f\n",valor_geral);
    printf("Comissão do vendedor: R$%2.2f\n",comissao);
    printf("Valor do objeto mais vendido R$%2.2f posição %d\n",vetor_precos[indice], indice+1);
}



int main(){
    LerPrecosQuantidades();
    Relatorio();
    return 0;
}