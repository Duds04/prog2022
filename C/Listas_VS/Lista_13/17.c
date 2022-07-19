#include <stdio.h>
#include <stdlib.h>
#include <math.h>
float informa(int l1, int l2, int l3);

int main(){
    int l1, l2, l3;

    printf("Escreva: ");
    scanf("%d %d %d", &l1, &l2, &l3);
    // equilátero 0, escaleno 1 ou isósceles 2
    printf("\nResultado: %f", informa(l1,l2,l3)); 

    return 0;
}

void informa(int l1, int l2, int l3){

    if(l1==l2 && l2==l3){
        printf("equilátero")
        return 0;
    }else if(l1!=l2 && l2!=l3 && l1!=l3){
        printf("escaleno")
        return 1;
    }else if((l1==l2 && l2!=l3) || (l3==l2 && l2!=l1) || (l3==l1 && l2!=l1)){
        printf("isósceles")
        return 2;
    }

    return -1;
}