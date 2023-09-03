#include <stdio.h>

int main (void)
{
    int range = 1000; //Variable to control range of Fizzbuzz
    int count = 0; //Challange Counter Variable 
    for (int i = 1; i < range; i++)
    {
        if ( i % 3 == 0 && i % 5 == 0)
        {
            printf("fizzbuzz\n");
            count += i; // Add the value of I if divisable by 3 AND 5 to count 
        }
        else if (i % 3 == 0)
        {
            printf("Fizz\n");
            count += i;// Add the value of I if divisable by 3 to count 

        }
        else if (i % 5 == 0)
        {
            printf("Buzz\n");
            count += i;// Add the value of I if divisable by 5 to count 
        }
        else
        {
            printf("%i\n", i);
        }
    }

    printf("Fizzbuzz Count = %i\n", count);//Display count value tested with given example range 10, count = 23. 
    //value when range = 1000, count = 23316
}
