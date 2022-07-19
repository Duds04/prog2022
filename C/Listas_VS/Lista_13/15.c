#include <stdio.h>
#include <stdlib.h>
#include <math.h>
double converte(int x,int y,int z, int x2,int y2,int z2);

int main(){
    int x, y, z, x2, y2, z2;

    printf("Escreva: ");
    scanf("%d %d %d", &x, &y, &z, &x2, &y2, &z2);
    printf("\nResultado: %lf", converte(x, y, z, x2, y2, z2));

    return 0;
}

double converte(int x,int y,int z, int x2,int y2,int z2){
    double d = 0;
    
    d = sqrt(pow((x2-x),2) + pow((y2-y),2) + pow((z2-z),2));

    return d;
}