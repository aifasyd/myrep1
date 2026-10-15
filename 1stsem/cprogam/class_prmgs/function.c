#include<stdio.h>

int rollno, eng, maths, python, dbms, evs;
int total;
float average, cgpa;

void getStudentData(){
    printf("Enter roll number: ");
    scanf("%d", &rollno);

    printf("Enter marks in English: ");
    scanf("%d", &eng);

    printf("Enter marks in Maths: ");
    scanf("%d", &maths);

    printf("Enter marks in Python: ");
    scanf("%d", &python);

    printf("Enter marks in DBMS: ");
    scanf("%d", &dbms);

    printf("Enter marks in EVS: ");
    scanf("%d", &evs);
}

void getTotal(){
    total = eng + maths + python + dbms + evs;
}

void getAverage(){
    average = total / 5.0;
}

void getCGPA(){
    cgpa = average / 9.5;
}

void displayStudentDetails(){
    printf("\n--- Student Report ---\n");
    printf("Roll No: %d\n", rollno);
    printf("Total Marks: %d\n", total);
    printf("Average: %.2f\n", average);
    printf("CGPA: %.2f\n", cgpa);
}

int main(){
    getStudentData();
    getTotal();
    getAverage();
    getCGPA();
    displayStudentDetails();

    return 0;
}