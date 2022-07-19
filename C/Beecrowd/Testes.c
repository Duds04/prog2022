#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int resolveEquacao(int a, int b, int c);

int main(){
    printf("01: %d %d \n", resolveEquacao(1, -4, -5));

    return 0;
}

int resolveEquacao(int a, int b, int c){
    int delta, raizDelta, raiz1, raiz2;
    delta = 0;
    raiz1 = 0;
    raiz2  = 0;

    delta = pow(b,2) + (-4 * a * c);
    raizDelta = (int) sqrt(delta);

    if(delta<0){
        printf("ERRO!\nDelta menor que 0\n");
        return -1;
    }
    
    raiz1 = (int) (((b) + raizDelta)/(a*2));
    raiz2 = (int) (((-b) - raizDelta)/(a*2));
    return raiz1, raiz2;
}