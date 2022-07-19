#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int menor(int n1, int n2, int n3);

int main(){
    int n1, n2, n3;

    printf("Escreva: ");
    scanf("%d %d %d", &n1, &n2, &n3);
    printf("\nResultado: %d", menor(n1, n2, n3));
    //menor(num);

    return 0;
}

int menor(int n1, int n2, int n3){
    int menor;
    menor = n1;

    if(menor>n2){
        if(n2<n3){
            menor = n2;
        }
    }
    if(menor>n3){
        menor = n3;
    }
    return menor;
}