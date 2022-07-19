#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int parImpar(int num);

int main(){
    int num; 
    printf("Escreva: ");
    scanf("%d", &num);
    if(parImpar(num)){
        printf("par");
    } 
    if(!parImpar(num)){
        printf("impar");
    } 
   
    return 0;
}

int parImpar(int num){
    if((num%2) == 0) return 1;
    else return 0;
}
