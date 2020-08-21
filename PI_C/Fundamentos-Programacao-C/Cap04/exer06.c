/*
Faça um programa que receba quatro valores: I, A, B e C. Desses valores, I é inteiro e positivo, A, B e
C são reais. Escreva os números A, B e C obedecendo à tabela a seguir.
Suponha que o valor digitado para I seja sempre um valor válido, ou seja, 1, 2 ou 3, e que os números
digitados sejam diferentes um do outro.
Valor de i

1 - A, B e C em ordem crescente.
2 - A, B e C em ordem decrescente.
3 - O maior fica entre os outros dois números.

*/
#include<stdlib.h>
#include<stdio.h>

int main(void){
    int option;
    float number1, number2, number3;
    do{
        printf("Digite o valor de I(INTEIRO), A(FLOAT), B(FLOAT), C(FLOAT) respectivamente.\n");
        scanf("%d %f %f %f", &option, &number1, &number2, &number3);
        if(option == 1){
            if (number1 >= number2 && number2 >= number3){
                printf("%.2f, %.2f, %.2f", number3, number2, number1);

            } else if(number1 >= number3 && number3 >= number2){
                printf("%.2f, %.2f, %.2f", number2, number3, number1);

            } else if(number2 >= number1 && number1 >= number3){
                printf("%.2f, %.2f, %.2f", number3, number1, number2);
                
            }else if(number2 >= number3 && number3 >= number1){
                printf("%.2f, %.2f, %.2f", number1, number3, number2);

            } else if( number3 >= number1 && number1 >= number2 ){
                printf("%.2f, %.2f, %.2f", number2, number1, number3);

            } else{
                printf("%.2f, %.2f, %.2f", number1, number2, number3);
            }
            
        } else if(option == 2){
            if (number1 >= number2 && number2 >= number3){
                printf("%.2f, %.2f, %.2f", number1, number2, number3);

            } else if(number1 >= number3 && number3 >= number2){
                printf("%.2f, %.2f, %.2f", number1, number3, number2);

            } else if(number2 >= number1 && number1 >= number3){
                printf("%.2f, %.2f, %.2f", number2, number1, number3);
                
            }else if(number2 >= number3 && number3 >= number1){
                printf("%.2f, %.2f, %.2f", number2, number3, number1);

            } else if( number3 >= number1 && number1 >= number2 ){
                printf("%.2f, %.2f, %.2f", number3, number1, number2);

            } else{
                printf("%.2f, %.2f, %.2f", number3, number2, number1);
            }
        } else if(option == 3){
            if (number1 >= number2 && number1 >= number3){
                printf("%.2f, %.2f, %.2f", number3, number1, number2);
            } else if(number2 >= number1 && number1 >= number3){
                printf("%.2f, %.2f, %.2f", number3, number2, number1);
            } else{
                printf("%.2f, %.2f, %.2f", number1, number3, number2); 
            }
            
        } 
        printf("\n");
        

    }while(option < 1 || option > 3);

    return 0;
}