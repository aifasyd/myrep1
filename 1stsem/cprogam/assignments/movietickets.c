#include<stdio.h>
int main(){  
    int n, category;
    int regular=0, premium=0, recliner=0;
    float total=0;

    printf("Enter number of tickets: ");
    scanf("%d", &n);

    for(int i=1; i<=n; i++){                // process each ticket one at a time
        printf("Enter category for ticket %d (1/2/3): ", i);
        scanf("%d", &category);

        while(category!=1 && category!=2 && category!=3){   // keep asking till input is correct
            printf("Invalid category. Please enter 1, 2, or 3: ");
            scanf("%d", &category);
        }

        
        switch(category){
            case 1:                         // Regular
                total = total + 150;
                regular++;
                break;
            case 2:                         // Premium
                total = total + 250;
                premium++;
                break;
            case 3:                         // Recliner
                total = total + 400;
                recliner++;
                break;
        }
    }

    printf("\n--- Final Bill ---\n");
    printf("Regular tickets: %d\n", regular);
    printf("Premium tickets: %d\n", premium);
    printf("Recliner tickets: %d\n", recliner);
    printf("Total (before discount): %.0f\n", total);

   
    if(n >= 5){
        float discount = total * 0.10;
        total = total - discount;
        printf("Discount applied: Yes\n");
    }
    else{
        printf("Discount applied: No\n");
    }

    printf("Final Amount: %.0f\n", total);
    return 0;
}