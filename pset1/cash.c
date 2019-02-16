// Implement a program that calculates the minimum number of coins required to give a user change.

// $ ./cash
// Change owed: 0.41
// 4

#include <cs50.h>
#include <math.h>
#include <stdio.h>

int main(void)
{
    int no0fCoins = 0;
    float input;
    int check = 0;
    do
    {
        input = get_float("How much change is owed?"); //get input from the user > 0
    }
    while (input < 0);

    input = input * 100; //to get the highest coins and ignore smallest
    check = round(input);  //round to ignore very small amount of pennies
    while (check % 25 != check) //!=check here because we will keep % till the output of % == output of check = check-25
    {
        check = check - 25;
        no0fCoins++;
    }
    while (check % 10 != check)
    {
        check = check - 10 ;
        no0fCoins++;
    }
    while (check % 5 != check)
    {
        check = check - 5;
        no0fCoins ++;
    }
    no0fCoins = no0fCoins + check ;
    printf("number of coins equal %i\n", no0fCoins);
}

// Another Solution

// #include <stdio.h>
// #include <cs50.h>
// #include <math.h>

// int main(void)
// {
//     int owed;
//     float ftOwed;
//     int numOfCoins = 0;
//     do
//     {
//         ftOwed = get_float("Enter how much we owe to you: ");
//     }
//     while (ftOwed < 0);
//     ftOwed *= 100;
//     owed = round(ftOwed);
//     // Checking if owed have 25 coin
//     while (owed >= 25)
//     {
//         owed -= 25;
//         numOfCoins += 1;
//     }
//     // checking if owed have 10 coin
//     while (owed >= 10)
//     {
//         owed -= 10;
//         numOfCoins += 1;
//     }
//     // checking if owed have 5 coin
//     while (owed >= 5)
//     {
//         owed -= 5;
//         numOfCoins += 1;
//     }
//     // Checking if owed have 1 coin
//     while (owed != 0)
//     {
//         owed -= 1;
//         numOfCoins += 1;
//     }
//     printf("%i\n", numOfCoins);
// }
