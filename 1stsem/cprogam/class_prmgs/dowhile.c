#include<stdio.h>
int main(){
    int choice;
    float num1, num2, result;

    printf("------welcome to my calculator--------\n");

    do{
        printf("1. addition\n");
        printf("2. subtraction\n");
        printf("3. multiplication\n");
        printf("4. division\n");
        printf("5. exit\n");

        printf("enter your choice:");
        scanf("%d", &choice);

        if(choice == 1){
            printf("enter first number: ");
            scanf("%f", &num1);
            printf("enter second number: ");
            scanf("%f", &num2);
            result = num1 + num2;
            printf("the sum is %.0f\n", result);
        }
        if(choice == 2){
            printf("enter first number: ");
            scanf("%f", &num1);
            printf("enter second number: ");
            scanf("%f", &num2);
            result = num1 - num2;
            printf("the difference is %.0f\n", result);
        }
        if(choice == 3){
            printf("enter first number: ");
            scanf("%f", &num1);
            printf("enter second number: ");
            scanf("%f", &num2);
            result = num1 * num2;
            printf("the product is %.0f\n", result);
        }
        if(choice == 4){
            printf("enter first number: ");
            scanf("%f", &num1);
            printf("enter second number: ");
            scanf("%f", &num2);
            result = num1 / num2;
            printf("the quotient is %.0f\n", result);
        }
        if(choice == 5){
            printf("program terminated.\n");
        }

    }while(choice != 5);

    printf("--------end-----------\n");

    return 0;
}