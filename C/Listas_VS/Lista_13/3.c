#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int primo(int num);

int main(){
    //while (1)
    //{
    int num; 
    printf("Escreva: ");
    scanf("%d", &num);
        //if(num<0) break;
    if(primo(num)){
        printf("E primo\n");
    } 
    if(!primo(num)){
        printf("Nao e primo\n");
    }    
    //}
    return 0;
    
}

int primo(int num){
    for (int i = 2; i < num; i++)
    {
        if((num%i) == 0) return 0; 
    }
    
    return 1;
}
