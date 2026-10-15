#include<stdio.h>

int main(){

    int x=10;     // x strores 10
    int*p;        // declare a pointer 
    p=&x;         // initialize pointer p to store the address of x 

    printf("%d\n",x);     // prints x 
    printf("%p\n",&x);    // prints the address using &x
    printf("%p",p);       // prints the address using the pointer 

    return 0;

}