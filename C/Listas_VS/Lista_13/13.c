#include <stdio.h>
#include <stdlib.h>
#include <math.h>
long long int valida(int num);
//int menor(int n1, int n2, int n3);

int main(){
    long int numCompleto;
    
    printf("Escreva: ");
    scanf("%ld", &numCompleto);


    printf("\nResultado: %lld", valida(numCompleto));
    //valida(num);

    return 0;
}

long long int valida(int num){
    int v[30], aux, soma;
    long long int guarda;
    aux = 100000000;
    guarda = num;
    soma = 0;

    for (int i = 0; i < 9; i++){
        v[i] = guarda / aux;
        guarda -= v[i]* aux; 
        aux = aux / 10;
        v[i] =  v[i] * (10-i);
        soma += v[i];
    }

    printf("%d", soma);

    int ve1, divide, ve2, soma2;
    divide = (int)soma/11;
    if(soma%11<2){
        ve1 = 0;
    }else{
        ve1 = divide - 11;
    }

    guarda = (num*10) + ve1;
    soma2 = 0;
    aux = 1000000000;
    for (int i = 0; i < 10; i++){
        v[i] = guarda / aux;
        guarda -= v[i]* aux; 
        aux = aux / 10;
        v[i] =  v[i] * (11-i);
        soma2 = soma2 + v[i];
    }

    divide = (int)soma2/11;
    if(soma2%11<2){
        ve2 = 0;
    }else{
        ve2 = 11 - (soma2%11);
    }

    guarda = (num*100) + ve2 + (ve1*10);
    return guarda;
}