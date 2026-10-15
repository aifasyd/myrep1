#include<stdio.h>

/* Reads one mark and keeps asking until it is between 0 and 100 */
int getValidMark(int subject){
    int mark;
    printf("  Subject %d marks (0-100): ", subject);
    scanf("%d", &mark);

    while(mark < 0 || mark > 100){
        printf("  Invalid! Enter marks between 0 and 100: ");
        scanf("%d", &mark);
    }
    return mark;
}

/* Reads roll number, name and 5 subject marks for all 5 students.
   Each student's name uses 30 characters of the name array:
   student 0 starts at name[0], student 1 at name[30], student 2 at name[60] ... */


void readStudentData(int rollNo[], char `name[], int sub1[], int sub2[], int sub3[], int sub4[], int sub5[]){
    for(int i=0; i<5; i++){
        printf("\nStudent %d\n", i+1);

        printf("  Roll number: ");
        scanf("%d", &rollNo[i]);

        printf("  Name: ");
        scanf(" %29[^\n]", &name[i*30]);   /* reads a full name (spaces allowed) into this student's 30-character slot */

        sub1[i] = getValidMark(1);
        sub2[i] = getValidMark(2);
        sub3[i] = getValidMark(3);
        sub4[i] = getValidMark(4);
        sub5[i] = getValidMark(5);
    }
}

// Total = sum of marks in all 5 subjects 
void calculateTotal(int sub1[], int sub2[], int sub3[], int sub4[], int sub5[], int total[]){
    for(int i=0; i<5; i++){
        total[i] = sub1[i] + sub2[i] + sub3[i] + sub4[i] + sub5[i];
    }
}

/* Average = Total / 5 */
void calculateAverage(int total[], float average[]){
    for(int i=0; i<5; i++){
        average[i] = total[i] / 5.0;
    }
}

// Percentage = (Total / 500) * 100 
void calculatePercentage(int total[], float percentage[]){
    for(int i=0; i<5; i++){
        percentage[i] = (total[i] / 500.0) * 100;
    }
}

// passed[i] = 1 if the student scored at least 35 in EVERY subject, otherwise 0 
void determineResult(int sub1[], int sub2[], int sub3[], int sub4[], int sub5[], int passed[]){
    for(int i=0; i<5; i++){
        if(sub1[i] < 35 || sub2[i] < 35 || sub3[i] < 35 || sub4[i] < 35 || sub5[i] < 35){
            passed[i] = 0;
        }
        else{
            passed[i] = 1;
        }
    }
}

// Prints the result table for all 5 students 
void displayResultTable(int rollNo[], char name[], int sub1[], int sub2[], int sub3[], int sub4[], int sub5[],
                        int total[], float average[], float percentage[], int passed[]){
    printf("\n");
    printf("---------------------------------------------------------------------------------------------\n");
    printf("%-8s%-20s%-6s%-6s%-6s%-6s%-6s%-8s%-9s%-10s%s\n",
           "Roll No", "Name", "S1", "S2", "S3", "S4", "S5", "Total", "Average", "Percent", "Result");
    printf("---------------------------------------------------------------------------------------------\n");

    for(int i=0; i<5; i++){
        printf("%-8d%-20s", rollNo[i], &name[i*30]);
        printf("%-6d%-6d%-6d%-6d%-6d", sub1[i], sub2[i], sub3[i], sub4[i], sub5[i]);
        printf("%-8d%-9.2f%-10.2f", total[i], average[i], percentage[i]);

        if(passed[i] == 1){
            printf("PASS\n");
        }
        else{
            printf("FAIL\n");
        }
    }
    printf("---------------------------------------------------------------------------------------------\n");
}

int main(){
    // all arrays are initialized to 0 first 
    int rollNo[5] = {0};
    char name[150] = {0};
    int sub1[5] = {0};
    int sub2[5] = {0};
    int sub3[5] = {0};
    int sub4[5] = {0};
    int sub5[5] = {0};
    int total[5] = {0};
    float average[5] = {0};
    float percentage[5] = {0};
    int passed[5] = {0};

    readStudentData(rollNo, name, sub1, sub2, sub3, sub4, sub5);
    calculateTotal(sub1, sub2, sub3, sub4, sub5, total);
    calculateAverage(total, average);
    calculatePercentage(total, percentage);
    determineResult(sub1, sub2, sub3, sub4, sub5, passed);
    displayResultTable(rollNo, name, sub1, sub2, sub3, sub4, sub5, total, average, percentage, passed);

    return 0;
}