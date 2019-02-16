//Implement a program that prints out a half-pyramid of a specified height

#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int height = get_int("Enter height of mario pyramid: "); //get integer height from user
    while (height < 0 || height > 23) //range of height
    {
        printf("Wrong\n");
        height = get_int("Enter Valid Height between 0 and 23: "); //keep getting height till it valid
    }
    for (int i = 0 ; i < height ; i++) //i for loop over height number
    {
        for (int j = 0 ; j < height - i - 1 ; j++) //j for printing spaces
        {
            printf(" ");
        }
        for (int n = 0 ; n < i + 2; n++) //n for printing hashes
        {
            printf("#");
        }
        printf("\n");
    }
}
