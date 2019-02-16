//Implement a program that prints out a double half-pyramid of a specified height, per the below.

//$ ./mario
//Height: 4
//   #  #
//  ##  ##
// ###  ###
//####  ####

#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int height;
    do
    {
        height = get_int("Please enter the height of 2 pyramids: ");
    }
    while (height < 0 || height > 23);
    // the main loop for the whole pyramid
    for (int i = 0; i < height; i++)
    {
        // Loop to print the left spaces
        for (int j = 0; j < (height - i - 1); j++)
        {
            printf(" ");
        }
        // loop to print the left hashes
        for (int k = 0; k < (i + 1); k++)
        {
            printf("#");
        }
        printf("  ");
        // loop to print the right hashes
        for (int l = 0; l < (i + 1); l++)
        {
            printf("#");
        }
        printf("\n");
    }
}
