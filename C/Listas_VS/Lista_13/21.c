#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int soma(int* vetor, int n);
void printarVetor(int v[], int n);

int main(){
    int n = 3;
    int v[n]; //vetor já é um ponteiro

    for(int i=0; i<n; i++){
        printf("\nEscreva: ");
        scanf("%d", &v[i]);
    }

    printf("\nResult: %d", soma(v, n));
    return 0;
}

void printarVetor(int v[], int n){
    for(int i=0; i<n; i++){
        printf("%d ", v[i]);
    }
    printf("\n");
}

int soma(int* v, int n){
    int soma =0;

    for (int i = 0; i < n; i++)
    {
        soma += pow(v[i],2);
    }

    return soma;
    
}
