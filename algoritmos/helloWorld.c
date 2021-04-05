#include <stdio.h>
#include<stdlib.h>
int main()
{
    int *p_n, *p_m, m, n;
    p_n = &n;
    p_m = &m;

    scanf("%d %d", p_n, p_m);
    printf("%d\n", *p_m * *p_n);
    return 0;
}
