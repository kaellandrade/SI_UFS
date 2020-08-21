#include<stdio.h>
/*
 A nota final de um estudante é calculada a partir de três notas atribuídas, respectivamente, a um trabalho
 de laboratório, a uma avaliação semestral e a um exame final. A média das três notas mencionadas
 obedece aos pesos a seguir.

 |          NOTA             | PESO
 | Trabalho de laboratório   |   2   
 |   Avaliação semestral     |   3
 |   Exame final             |   5

Faça um programa que receba as três notas, calcule e mostre a média ponderada
e o conceito que segue a tababela.

 |     MÉDIA PONDERADA       | CONCEITO
 |   entre 8,00 e 10,00      |   A   
 |   entre 7,00 e 8,00       |   B
 |   entre 6,00 e 7,00       |   C
 |   entre 5,00 e 6,00       |   D
 |   entre 0,0 e 5,00        |   E


*/
int main()
{
    float ntrabalho, navaliacao, nexame, mediapond;

    printf("Digite a nota do trabalho de lab: \n");
    scanf("%f", &ntrabalho);
    printf("Digite a nota da avaliação semestral: \n");
    scanf("%f", &navaliacao);
    printf("Digite a nota do exame final: \n");
    scanf("%f", &nexame);
    mediapond = ((ntrabalho * 2) + (navaliacao * 3) + (nexame * 5)) / 10; // Calculando a nota ponderada
    if (mediapond > 10){
        printf("Média inválida!\n");   
    } else if(mediapond >= 8)
    {
        printf("Média: %2.2f \nConceito: A\n", mediapond);
    }else if (mediapond >= 7)
    {
        printf("Média: %2.2f \nConceito: B\n", mediapond);
    }else if(mediapond >= 6)
    {
        printf("Média: %2.2f \nConceito: C\n", mediapond);
    } else if(mediapond >= 5)
    {
        printf("Média: %2.2f \nConceito: D\n", mediapond);
    } else
    {
        printf("Média: %2.2f \nConceito: E\n", mediapond);        
    }
    return 0;
}
