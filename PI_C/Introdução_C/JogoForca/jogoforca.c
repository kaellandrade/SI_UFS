#include<stdlib.h>
#include<time.h>
#include<stdio.h>
#include<string.h>
#include<math.h>
#include "forca.h"

char palavrasecreta[20];
char chutes[26];
int chutesdados = 0;

int enforcou(){
    int erros = 0;
    for(int i= 0; i < chutesdados;i++){
        int existe = 0;
        for(int j=0 ; j < strlen(palavrasecreta);j++){
            if(chutes[i] == palavrasecreta[j]){
                existe = 1;
                break;
            }
        }
        if(!existe) erros++;
    }
    return erros >= 5;

}

int ganhou(){
    for(int i = 0; i < strlen(palavrasecreta);i++){
        if(!jachutou(palavrasecreta[i])){
            return 0;
        }
    }
    return 1;
}

void abertura(){
    printf("***************\n");
    printf("*Jogo Da Forca*\n");
    printf("***************\n");
}


void chuta(){
    char chute;
    printf("Qual letra? ");
    scanf(" %c",&chute);
    chutes[chutesdados] = chute;
    chutesdados++;
}

int jachutou(char letra){
    int achou = 0;

    for (int j = 0; j < chutesdados; j++){
        if(chutes[j] == letra){
            achou = 1;
            break;
        }
    }
    return achou;
}



void desenhaforca(){
    printf("Você já deu %d chutes\n", chutesdados);
    for(int i = 0; i <strlen(palavrasecreta); i++){
        if(jachutou(palavrasecreta[i])){
            printf("%c ",palavrasecreta[i]);
        }else{
            printf("-- ");
        }
    }
    printf("\n");


}
void escolhepalavra(){
    int qtddepalavras;

    FILE* f;

    f = fopen("palavras.txt","r");
    if(f == 0){
        printf("Banco de dados de palavras não está disponível\n\n");
        exit(1);
    }

    fscanf(f, "%d",&qtddepalavras);
    srand(time(0));
    int randomico = rand() % qtddepalavras;

    for (int i = 0; i < randomico; i++)
    {
        fscanf(f,"%s", palavrasecreta);
    }
    fclose(f);
    

}

void adcionarpalavra(){
    char quer;

    printf("Deseja adicionar uma nova palavra no jogo? (S/N)?\n");
    scanf(" %c",&quer);

    if(quer == 'S'){
        char novapalavra[20];

        printf("Dite a nova palavra, em letras maiúsculas: \n");
        scanf("%s", novapalavra);

        FILE* f;

        // Abre arquivo
        f =fopen("palavras.txt","r+");
        if(f == 0){
            printf("Banco de dados de palavras não disponível\n\n");
            exit(1);
        }
        int qtd;
        fscanf(f, "%d", &qtd);
        qtd++;
        fseek(f, 0, SEEK_SET);
        fprintf(f, "%d", qtd);

        fseek(f,0,SEEK_END);
        fprintf(f, "\n%s", novapalavra);   
        // fecha

        fclose(f);
    }
}

int main() {
    abertura();
    escolhepalavra();
    
    do{
        desenhaforca();
        chuta();
       
    } while (!ganhou() && !enforcou()); // ENQUANTO NÃO ACERTAR E NÃO ENFORCAR.
    adcionarpalavra();
}

