#include <stdio.h>
#include <string.h>

int main() {
    char name[100];
    int len;

    printf("enter string : ");
    fgets(name, sizeof(name), stdin);

    printf("you entered: %s\n", name);

    return 0;

}