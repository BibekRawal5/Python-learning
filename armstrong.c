#include <stdio.h>

int main()
{
    int i, j, temp, sum, digit;
    for (i = 1; i <= 500; i++)
    {
        temp = i;
        sum = 0;
        while (temp > 0)
        {
            digit = (temp % 10);
            sum += digit * digit * digit;
            temp = temp/10;
        }
        
        if (sum == i)
        {
            printf("%d\n", i);
        }
        
    }
}