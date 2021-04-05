#include <stdio.h>
/**
 * Ler três valroes A,B e C que são as três notas 
 * de uma aluno. Calcule a média do aluno, sabendo que anoda A tem peso 2
 * a nota B tem peso 3 e anota C tem peso 5
*/

int main()
{
    float na, nb, nc, nota;

    scanf("%f %f %f", &na, &nb, &nc);

    nota = ((na * 2) + (nb * 3) + (nc * 5)) / 10;
    printf("Sua note é: %.2f\n", nota);
    return 0;
}