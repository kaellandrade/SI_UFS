#include<stdio.h>

int main(void){
    int idade, contasexoF,contasexoM, menorIdadeF, menor_com_exper, menor_idade_mulher, contasexoM_exper,conta_maior_45;
    float idade_media, perc, maior_de_45;
    char sexo;
    char exper;
    contasexoM_exper = 0;
    contasexoF = 0;
    contasexoM = 0;
    conta_maior_45 = 0;
    menor_com_exper =0;
    idade_media = 0;
    printf("Digite sua idade:\n");
    scanf("%d",&idade);
    printf("Digite seu sexo[F/M]:\n");
    scanf("%s",&sexo);
    printf("Você tem experiência no serviço[S/N]:\n");
    scanf("%s",&exper);
    if(sexo == 'F'){
        contasexoF += 1;
        if(exper == 'S'){
            menor_idade_mulher = idade;
            if(idade < 21){
                menor_com_exper += 1;
            }
            if(idade < menor_idade_mulher){
            menor_idade_mulher = idade;
            }
        }
        
    }else if(sexo == 'M'){
        contasexoM+=1;
        if (idade > 45){
            conta_maior_45+=1;
        }
        if(exper == 'S'){
            contasexoM_exper+=1;
            idade_media += idade;
        }
    }
    if(idade == 0){
        printf("Número de canditatos do sexo feminino: %d\n",contasexoF);
        printf("Número de canditatos do sexo masculino: %d\n",contasexoM);
        printf("Idade média dos homens com experiência no serviço: %d\n: %d", idade_media/contasexoM_exper);

        if(maior_de_45 == 0){
            printf("Nenhum homem.\n:");
        }else{
            printf("Porcentagem dos homens com mais de 45: %d\n:",contasexoM*100/maior_de_45);

        }
        printf("Mulheres menor de 21 anos e com experiência no serviço: %d\n",menor_com_exper);
        printf("Menor idade das mulheres que tem experiência no serviço: %d\n: %d\n",menor_idade_mulher);

    }

    while (idade != 0){
        printf("Digite sua idade:\n");
        scanf("%d",&idade);
        printf("Digite seu sexo[F/M]:\n");
        scanf("%s",&sexo);
        printf("Você tem experiência no serviço[S/N]:\n");
        scanf("%s",&exper);
        if(sexo == 'F'){
            contasexoF += 1;
            if (exper == 'S' && idade < 21){
                menor_com_exper += 1;
            }

            if(idade < menor_idade_mulher){
                menor_idade_mulher = idade;
            }
            
        }

    }
    printf("Número de canditatos do sexo feminino: %d\n",contasexoF);
    printf("Número de canditatos do sexo masculino: %d\n",contasexoM);
    printf("Idade média dos homens com experiência no serviço: %d\n: %d", idade_media/contasexoM_exper);

    if(maior_de_45 == 0){
        printf("Nenhum homem.\n:");
    }else{
        printf("Porcentagem dos homens com mais de 45: %d\n:",contasexoM*100/maior_de_45);

    }
    printf("Mulheres menor de 21 anos e com experiência no serviço: %d\n",menor_com_exper);
    printf("Menor idade das mulheres que tem experiência no serviço: %d\n: %d\n",menor_idade_mulher);
    
}