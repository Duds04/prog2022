#include <stdio.h>
#include <stdlib.h>
#include <math.h>
float calculaT(int n1, int n2, int n3);

int main(){
    int n1, n2, n3;

    printf("Escreva: ");
    scanf("%d %d %d", &n1, &n2, &n3);
    printf("\nResultado: %f", calculaT(n1,n2,n3));

    return 0;
}

float calculaT(int n1, int n2, int n3){
    float p, a;

    p = (n1 + n2 + n3)/3;

    a = sqrt(p*(p-n1)*(p-n2)*(p-n3));

    return a;
}