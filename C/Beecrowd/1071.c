#include <stdio.h>
#include <math.h>
int soma(int n, int n2);


int main(){
    int n1, n2;
    scanf("%d", &n1);
    scanf("%d", &n2);

    printf("%d\n",soma(n1, n2));

    return 0;
}

int soma(int n, int n2){
    int soma = 0;
    if(n>n2){
        for(int i=(n2+1); i<n; i++){
            if((i%2)!=0){
                soma+=i;
            }
        }
    }else{
        for(int i=(n+1); i<n2; i++){
            if((i%2)!=0){
                soma+=i;
            }
        }
    }
    return soma;
}