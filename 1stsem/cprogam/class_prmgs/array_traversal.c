#include<stdio.h>

int getSize(){
    int size;
    printf("Enter the size of the arrau(>4): ");
    scanf("%d", &size);
    return size;
}

int validateSize(int size){
    while(size <= 4){
        printf("Invalid size!!!! Enter a valid size(>4): ");
        scanf("%d", &size);
    }
    return size;
}

void getElements(int arr[], int size){
    for(int i=0; i<size; i++){
        if(i==0)
            printf("Enter 1st array element: ");
        else if(i==1)
            printf("Enter 2nd array element: ");
        else if(i==2)
            printf("Enter 3rd array element: ");
        else if(i==3)
            printf("Enter 4th array element: ");
        else
            printf("Enter %dth array element: ", i+1);

        scanf("%d", &arr[i]);
    }
}

int calculateSum(int arr[], int size){
    int sum=0;
    for(int i=0; i<size; i++){
        sum += arr[i];
    }
    return sum;
}

void displayResult(int arr[], int size, int sum){
    printf("\nArray elements : [");
    for(int i=0; i<size; i++){
        printf("%d", arr[i]);
        if(i != size-1){
            printf(", ");
        }
    }
    printf("]\n");

    printf("The sum of all elements: %d\n", sum);
}

int main(){
    int arr[100];

    int size = getSize();
    size = validateSize(size);

    getElements(arr, size);
    int sum = calculateSum(arr, size);
    displayResult(arr, size, sum);

    return 0;
}