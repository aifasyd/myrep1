#include <stdio.h>
int main(){
    int n, sum = 0;

    printf("Enter N value: ");
    scanf("%d", &n);

    if (n < 5) {
        printf("!! Please enter a valid input greater than 5\n !!");
    } else {
        for (int i = 5; i <= n; i++) {
            sum += i;
        }
        printf("Sum of numbers from 5 to %d is %d\n", n, sum);
    }

    return 0;
}                                                                                                                    