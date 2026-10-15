#include<stdio.h>
int main(){
    int j;
    for(int i=0;i<=5;i++){
        printf("loop started\n");
        for(j=0;j<5;j++){
            printf("inner loop started\n");
            break;
            printf("inside the loop\n");

    }
    printf("from outer floop\n");
    break;
    }
    printf("program terminanated\n");
    return 0;
}