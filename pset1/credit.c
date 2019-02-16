// Implement a program that determines whether a provided credit card number is valid according to Luhn’s algorithm.

// $ ./credit
// Number: 378282246310005
// AMEX

//check for validation of credit card number
#include <cs50.h>
#include <math.h>
#include <stdio.h>
#include <stdint.h> //this library allow me to use uint64_t or int64_t for 64bit integer
//any printf function exists was used just for checking and debugging.
int main(void)
{
    uint64_t cardNumber = 0; //assign cardNumber to integer that can have up to 64bit
    int x, y, z, x1, x2 = 0;
    int counter = 0; //to count how many digits had been eliminated.
    int calculator = 0; // to calculate the num of all numbers.
    do
    {
        cardNumber = get_long_long("Enter your credit card number ");
    }
    while (!cardNumber);
    while (cardNumber / 100 > 10) //we divide cardNumber by 100 compare to 10 to check when we will reach to last 2 or 3 digits.
    {
        x = cardNumber % 100;
        if (x < 10) //this will be used at condition of last 2 digits are 05 or 0 any number.
        {
            calculator += x;
            // printf("%i\n", calculator);
        }
        else
        {
            y = x % 10; // y resposible of getting last digit
            x = x / 10; // x here resposible of getting second to last digit
            x = x * 2;
            if (x >= 10) //this will be used to convert x*2 to first digit + second digit if x*2 >=10
            {
                x1 = x % 10;
                x2 = x / 10;
                x  = x1 + x2;
            }
            z = x + y ; //getting the result of multiply second to last digit by 2 and add it to last digit
            calculator += z;
        }
        cardNumber = cardNumber / 100;
        // printf("%lu\n", cardNumber);
        counter += 2;
        // printf("%i\n", counter);
    }
    if ((cardNumber > 100 && counter == 10) || (cardNumber > 100 && counter == 12)) //check for VISA or AMEX
    {
        x = cardNumber % 10;
        calculator += x;
        y = cardNumber / 10;
        if ((y == 34 && counter == 12) || (y == 37 && counter == 12))
        {
            x = y % 10;
            x = x * 2;
            if (x > 10)
            {
                x1 = x % 10;
                x2 = x / 10;
                x  = x1 + x2 ;
            }
            calculator += x;
            y = y / 10;
            calculator += y;
            if (calculator % 10 == 0)
            {
                printf("AMEX\n");
            }
            else
            {
                printf("INVALID\n");
            }
        }
        else if (cardNumber % 100 == 4 && counter == 10)
        {
            x = y % 10;
            x = x * 2;
            if (x > 10)
            {
                x1 = x % 10;
                x2 = x / 10;
                x  = x1 + x2 ;
            }
            calculator += x;
            y = y / 10;
            calculator += y;
            if (calculator % 10 == 0)
            {
                printf("VISA\n");
            }
            else
            {
                printf("INVALID\n");
            }
        }
        else
        {
            printf("INVALID\n");
        }
    }
    else if (cardNumber < 100 && counter == 14)
    {
        y = cardNumber % 10;
        x = cardNumber / 10;
        x = x * 2;
        if (x >= 10)
        {
            x1 = x % 10;
            x2 = x / 10;
            x = x1 + x2;
        }
        calculator += y;
        // printf("%i\n", calculator);
        calculator += x;
        // printf("%i\n", calculator);
        if (calculator % 10 == 0)
        {
            if (cardNumber == 51 || cardNumber == 52 || cardNumber == 53 || cardNumber == 54 || cardNumber == 55)
            {
                printf("MASTERCARD\n");
            }
            else if (cardNumber / 10 == 4)
            {
                printf("VISA\n");
            }
            else
            {
                printf("INVALID\n");
            }
        }
        else
        {
            printf("INVALID\n");
        }
    }
    else
    {
        printf("INVALID\n");
    }
}
