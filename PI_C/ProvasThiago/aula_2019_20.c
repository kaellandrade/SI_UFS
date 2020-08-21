#include<stdlib.h>
#include<stdio.h>

int main(void){
    
    /*
    // Questão 4
    int num, fat;
    for (int i = 1; i <= 10; i++){
        scanf("%d",&num);
        fat = 1;
        for (int j = 1; j <= num; j++){
            fat *= j;
        }
        printf("%d\n",fat);

    }
    */

    /*
    // Questão 3
    int n,maior, menor;
    printf("Digite o 1º valor:\n");
    scanf("%d",&n);
    maior = n;
    menor = n;
    
    for(int i = 2; i<=5;i++){
        printf("Digite o %dº valor:\n",i);
        scanf("%d",&n);

        if(n > maior){
            maior = n;
        }
        if(n < menor){
            menor = n;
        }
    }
    printf("Maior = %d\nMenor = %d\n",maior,menor);
    */

/*
    // Questão 02
    int horainicio, minutoinicio, horafinal, minutofinal, horatotal, minutototal;
    scanf("%d %d",&horainicio, &minutoinicio);
    scanf("%d %d",&horafinal, &minutofinal);
    if(minutofinal < minutoinicio){
        minutofinal = minutofinal + 60;
        horafinal = horafinal - 1;
    }
    if(horafinal < horainicio){
        horafinal = horafinal+24;
    }
    
    horatotal = horafinal - horainicio;
    minutototal = minutofinal - minutoinicio;
    printf("%d:%.2d\n",horatotal,minutototal);
*/

    /*
    // Questão 01
    float salario,percentual,salfinal;
    printf("Digite o salário\n");
    scanf("%f",&salario);
    printf("Digite o percentual\n");
    scanf("%f",&percentual);
    salfinal = salario + (salario * percentual/100.0);
    printf("Salário final = %.2f\n",salfinal);
    return 0;
    */
}
