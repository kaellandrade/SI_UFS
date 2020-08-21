#include<stdio.h>

int main(void){
    #define TOTALALUNOS 6
    float nota1,nota2,mediaAluno, mediaClasse; 
    int totApro=0; 
    int totRepro=0; 
    int totExa=0;
    int totclasse=0;

    for(int i=1; i<=TOTALALUNOS;i++){
        scanf("%f %f",&nota1, &nota2);
        mediaAluno = (nota1 + nota2)/2.0;
        printf("Média do aluno:%2.2f \n",mediaAluno);
        if(mediaAluno<=3){
            printf("Reprovado.\n");
            totRepro += 1;

        }else if(mediaAluno <=7){
            printf("Exames.\n");
            totExa += 1;

        }else{
            printf("Aprovado.\n");
            totApro += 1;

        }
        totclasse+=mediaAluno;
    }
    mediaClasse = totclasse/TOTALALUNOS;
    printf("Total de alunos aprovados: %d\n",totApro);
    printf("Total de alunos em exames: %d\n", totExa);
    printf("Total de alunos reprovados: %d\n", totRepro);
    printf("Média da classe: %2.2f\n", mediaClasse);


    
}