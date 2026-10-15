#include <stdio.h>
int main(){
    // Ascending part
    for (int i = 1; i <= 5; i++) {
        for (int j = 1; j <= i; j++) {
            printf("%d ", j);
        }
        printf("\n");
    }


    printf("\n");

    // Descending part (5 down to 1)
    for (int i = 5; i >= 1; i--) {
        for (int j = 1; j <= i; j++) {
            printf("%d ", j);
        }
        printf("\n");
    }

    printf("\n");

    // Descending part with blanks in specific rows
    for (int i = 5; i >= 1; i--) {
        for (int j = 1; j <= i; j++) {
            if (i == 5 && j == 3) {
                printf("  ");
            } else if (i == 3 && j == 2) {
                printf("  ");
            } else {
                printf("%d ", j);
            }
        }
        printf("\n");
    }

    return 0;
}