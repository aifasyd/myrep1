#include<stdio.h>
int main(){
    int accountno = 1000;
    float balance = 500;
    float amount;
    int choice;
    int entered_acc;

    printf("----welcome to my bank----\n");

    do{
        printf("1. Deposit\n2. Withdraw\n3. Check Balance\n4. Exit\n");
        printf("Enter choice: ");
        scanf("%d", &choice);

        if(choice != 4){
            printf("Enter account number: ");
            scanf("%d", &entered_acc);

            if(entered_acc == accountno){
                printf("Valid account!\n");

                switch(choice){
                    case 1:
                        printf("Enter amount to deposit: ");
                        scanf("%f", &amount);
                        balance += amount;
                        printf("Account updated. New balance: %.2f\n", balance);
                        break;

                    case 2:
                        printf("Enter amount to withdraw: ");
                        scanf("%f", &amount);
                        if(amount > balance)
                            printf("Insufficient balance!\n");
                        else {
                            balance -= amount;
                            printf("Account updated. New balance: %.2f\n", balance);
                        }
                        break;

                    case 3:
                        printf("Current balance: %.2f\n", balance);
                        break;

                    default:
                        printf("Invalid choice!\n");
                }
            }
            else {
                printf("Invalid account number!\n");
            }
        }
        else{
            printf("Exiting...\n");
        }

    }while(choice != 4);

    printf("Thank you for banking with us!\n");

    return 0;
}