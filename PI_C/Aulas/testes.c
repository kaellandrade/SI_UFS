#include<stdio.h>

int main()
{
    float n1, n2, n3, media, exame;
    printf("Nota 1\n");
    scanf("%f",&n1);
    printf("Nota 2\n");
    scanf("%f",&n2);
    printf("Nota 3\n");
    scanf("%f",&n3);
    media = (n1+n2+n3)/3.0;
    if(media > 7 || media < 0){
        printf("Média inválida!\n");
    } else if (media >= 7){
        printf("Aprovado com média: %2.2f\n", media);
    } else if(media >= 3){
        exame = 12 - media;
        printf("Sua média foi %2.2f %2.2f no exame!\n", media,exame);
    } else{
        printf("Reprovado com média: %2.2f\n",media);
    }
    return 0;
}
