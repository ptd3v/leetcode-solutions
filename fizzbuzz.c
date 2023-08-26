#include <stdio.h>

int main (void)
{
    int range = 21;
    int count = 0;
    for (int i = 0; i < range; i++)
    {
        if ( i % 3 = 0 && i % 5 = 0)
        {
            printf("fizzbuzz\n");
            count += i;
        }
        else if (i % 3 = 0)
        {
            printf("Fizz\n");
            
        }
        else if (i % 5 = 0)
        {
            printf("Buzz\n");
        }
        else 
        {
            printf("d%\n");
        }
    }

    printf("Fizzbuzz Count = %d", count);
}
