#include<stdio.h>
int main(){
    float s1sub1, s1sub2, s1sub3, s1total, s1perc;
    float s2sub1, s2sub2, s2sub3, s2total, s2perc;
    float s3sub1, s3sub2, s3sub3, s3total, s3perc;
    float sub1, sub2, sub3;
    int student = 1;

    printf("---- STUDENT RESULT CALCULATOR ----\n");

    do{
        printf("\nEnter marks for Student %d\n", student);

        printf("maths (0-100): ");
        scanf("%f", &sub1);
        printf("python (0-100): ");
        scanf("%f", &sub2);
        printf("dbms (0-100): ");
        scanf("%f", &sub3);

        switch(student){
            case 1:
                s1sub1=sub1; s1sub2=sub2; s1sub3=sub3;
                s1total = sub1+sub2+sub3;
                s1perc = s1total/3;
                break;
            case 2:
                s2sub1=sub1; s2sub2=sub2; s2sub3=sub3;
                s2total = sub1+sub2+sub3;
                s2perc = s2total/3;
                break;
            case 3:
                s3sub1=sub1; s3sub2=sub2; s3sub3=sub3;
                s3total = sub1+sub2+sub3;
                s3perc = s3total/3;
                break;
        }

        student++;

    }while(student <= 3);

    printf("\n----------------------------------------------------------\n");
    printf("Student  maths    python    dbms    Total   Percent  Result\n");
    printf("----------------------------------------------------------\n");

    printf("%-8d %-7.2f %-7.2f %-7.2f %-7.2f %-8.2f ", 1, s1sub1, s1sub2, s1sub3, s1total, s1perc);
    if(s1sub1<35 || s1sub2<35 || s1sub3<35){
        printf("FAIL\n");
    }
    else{
        printf("PASS\n");
    }

    printf("%-8d %-7.2f %-7.2f %-7.2f %-7.2f %-8.2f ", 2, s2sub1, s2sub2, s2sub3, s2total, s2perc);
    if(s2sub1<35 || s2sub2<35 || s2sub3<35){
        printf("FAIL\n");
    }
    else{
        printf("PASS\n");
    }

    printf("%-8d %-7.2f %-7.2f %-7.2f %-7.2f %-8.2f ", 3, s3sub1, s3sub2, s3sub3, s3total, s3perc);
    if(s3sub1<35 || s3sub2<35 || s3sub3<35){
        printf("FAIL\n");
    }
    else{
        printf("PASS\n");
    }

    printf("----------------------------------------------------------\n");
    printf("Thank you for using the calculator!:))\n");

    return 0;
}