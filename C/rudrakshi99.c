#include <stdio.h>
#include <string.h>

void CodeToCoffee(char str[], int n)
{
    int index = 0;

    for (int i = 0; i < n; i++)
    {

        int j;
        for (j = 0; j < i; j++)
            if (str[i] == str[j])
                break;

        if (j == i)
            str[index++] = str[i];
        if (str[index] == 'f')
        {
            str[index] = 'd';
        }
    }

    printf("\n Your Coffee becomes %s \n\n\n", str);
}

int main()
{
    char str[] = "coffee";
    int n = sizeof(str) / sizeof(str[0]);
    CodeToCoffee(str, n);

    return 0;
}