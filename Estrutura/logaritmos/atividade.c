#include <math.h>
#include <stdio.h>

//? 1. Critique a seguinte versão da função lg.
//? Ela usa as funções log10 e floor da biblioteca math

/*  
* R: Poderíamos apenas calcular o log2(N), ao ínves de log10(N)/log10(2);
* pois logb (X) / logb (A) == logA (X)
*/

int lg(int N) {
    double x;
    x = log2(N);
    return floor(x);
}

//? 2. Mostre que o código abaixo corre o risco de produzir resultados
//? errados em virtudes de overflow aritmético //
//* R:Temos que log2(0) não está definido, e essa função retorna -1.
int lgii(int N) {
    int i = 0, n = 1;
    while (n <= N){
        n = 2 * n;
        i += 1;
    }
    return i - 1;
}

//?  3. Verifique que a seguinte versão alternativa da função lg está correta:
int lgiii(int N){
    int i = 0;
   for (int n = 2; n <= N; n = 2*n) 
      i += 1;
   return i;
}

//? 4. Critique a seguinte versão alternativa da função lg:
//  * R. Uso desnecessário da condicional if dentro do while, o que pode comprometer
//  * a eficiência do código. Esse código poderia ser refatorado da seguinte forma 
//  * while (N > n).... sem a necessidade da flag achou
int lgiv(int N) {
     int achou = 0, i = 0, n = 1;
    while (!achou) {
      n *= 2;
      i += 1;
      if (n > N) achou = 1;
   }
   return i - 1;
}


// ? 5. Critique a seguinte versão alternativa da função lg
int lgv(int N){
    if (N == 1) return 0;
    if (N == 2) return 1;
    int i = 2;
    int n = 4;
    while(n <= N) {
        n = 2 * n;
        i += 1;
    }
    return i - 1;

}

//? 6.  Eficiência.  Critique a seguinte versão alternativa da função lg. 
//? Ela calcula, explicitamente, a maior potência de 2 que não passa de N. 
/* //! Não entendi
int potencia (int i) { 
   int p = 1;
   for (int j = 1; j <= i; ++j) {
       p = 2 * p;
    }
   return p;
}
int lgvi (int N) {
   for (int i = 0; potencia (i) <= N; ++i) {}
    return i - 1;    
}
*/

//? 7. Logaritmos na base 10.  Escreva uma função que calcule o piso do logaritmo na base 10 de um número.

// Dado um numero natural N log10Piso calcula o piso de N
// na base 10
int log10Piso(int N){
    int i = 0;
    int n = 1;
    int x = N / 10;

    while(n <= N/10){
        n = n * 10;
        i++;
    }
    return i;
}

int teste (int N)
{  
   int i, n;
   i = 0;
   n = 1;
   while (n <= N/2) {
      n = 2 * n;
      i += 1;
   }
   return i;    
}


int main() {
    printf("lg -> %d\n", lg(10)); // Invocando lg
    printf("lgii -> %d\n", lgii(10)); // Invocando lgII
    printf("lgiii -> %d\n", lgiii(10)); //  Invocando lgIII
    printf("lgiv -> %d\n", lgiv(10)); //  Invocando lgIV
    printf("lgv -> %d\n", lgv(10)); //  Invocando lgV
    // printf("lgvi -> %d\n", lgvi(10)); //Invocando lgVI
    printf("log10Piso -> %d\n ", log10Piso(10));
    printf("teste -> %d\n ", teste(10));



    return 0;
}

