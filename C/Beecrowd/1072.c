#include <stdio.h>
#include <math.h>

int main(){
    int n, x, dentro, fora;
    dentro = 0;
    fora = 0;

    scanf("%d", &n);

    for(int i=0; i<n; i++){
        scanf("%d", &x);
        if(x>=10 && x<=20){
            dentro+=1;
        }else{
            fora+=1;
        }
    }

    printf("%d in\n", dentro);
    printf("%d out\n", fora);

    return 0;
}
