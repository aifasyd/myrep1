#include <stdio.h>
#include <string.h>

int main() {
    char names[50] = "aifa syed ismail";
    for (int i = 0; i < strlen(names); i++) {
        printf("%c ", names[i]);
    }

    char word[50];
    printf("\nenter word: ");
    scanf("%49s", word);
    printf("word is %s",word);

    return 0;
}