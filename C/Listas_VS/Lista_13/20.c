#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int div3(int* vetor, int n);
void printarVetor(int v[], int n);

int main(){
    int n = 5;
    int v[n]; //vetor já é um ponteiro

    for(int i=0; i<n; i++){
        printf("\nEscreva: ");
        scanf("%d", &v[i]);
    }

    div3(v, n);
    return 0;
}

void printarVetor(int v[], int n){
    for(int i=0; i<n; i++){
        printf("%d ", v[i]);
    }
    printf("\n");
}

int div3(int* v, int n){
    for (int i = 0; i < n; i++)
    {
        if(v[i]%3 == 0){
            printf("%d e divisivel por 3\n", v[i]);
        }
    }

    return 0;
    
}
