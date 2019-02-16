// Helper functions for music

#include <cs50.h>
#include "helpers.h"
#include <math.h>
#include <string.h>

int define_value_of_frequency(int a);
float charcter_definiton(char a);
// Converts a fraction formatted as X/Y to eighths
int duration(string fraction)
{
    // TODO
    int numerator = fraction[0] - 48;
    int denominator = fraction[2] - 48;
    if (numerator == 1 && denominator == 8)
    {
        return 1;
    }
    else if (numerator == 1 && denominator == 4)
    {
        return 2;
    }
    else if (numerator == 1 && denominator == 2)
    {
        return 4;
    }
    else if (numerator == 3 && denominator == 8)
    {
        return 3;
    }
    else
    {
        return 0; //if we tried to compile this, compiler will not accept because we didnt assign all possibilites of return to avoid program from freezing
    }
}
// Calculates frequency (in Hz) of a note
int frequency(string note)
{
    // TODO
    if (note[0] == 'A')
    {
        if (note[1] != '#' && note[1] != 'b')
        {
            int a = note[1] - 48;
            return define_value_of_frequency(a);
        }
        else
        {
            int a = note[2] - 48;
            if (note[1] == '#')
            {
                return round(define_value_of_frequency(a) * pow(2, 0.0833333333333333)); //1/12
            }
            else
            {
                return round(define_value_of_frequency(a) / pow(2, 0.0833333333333333)); //1/12
            }
        }
    }
    else
    {
        if (note[0] == 'B')
        {
            if (note[1] != '#' && note[1] != 'b')
            {
                int a = note[1] - 48;
                return round(define_value_of_frequency(a) * pow(2, 0.1666666666666667));
            }
            else
            {
                int a = note[2] - 48;
                return round(define_value_of_frequency(a) * pow(2, 0.0833333333333333));
            }
        }
        else
        {
            float n = charcter_definiton(note[0]); // getting value of interval depending on char by user
            float x = n / 12; // divide the value of musical intervals depending on character input by 12
            if (note[1] == '#')
            {
                return round(define_value_of_frequency(note[2] - 48) * pow(2, 0.0833333333333333) / pow(2, x)); // at case that input has #
            }
            else if (note[1] == 'b')
            {
                return round(define_value_of_frequency(note[2] - 48) / pow(2, 0.0833333333333333) / pow(2, x)); //at case that input has b
            }
            else
            {
                return round(define_value_of_frequency(note[1] - 48) / pow(2, x)); //at case that input has no # or b
            }
        }
    }
}
// Determines whether a string represents a rest
bool is_rest(string s)
{
    // TODO
    if (s == "" || s[0] == '\0')
    {
        return true;
    }
    else
    {
        return false;
    }
}
//defining value of frequency depending on octave and just move to equivalent A not final frequency
int define_value_of_frequency(int a)
{
    if (a == 4)
    {
        return 440;
    }
    else
    {
        if (a < 4)
        {
            a = 4 - a ;
            return 440 / pow(2, a);
        }
        else
        {
            a = a - 4;
            return 440 * pow(2, a);
        }
    }
}
// defining the character depending on the input
float charcter_definiton(char a)
{
    if (a == 'G')
    {
        return 2;
    }
    else if (a == 'F')
    {
        return 4;
    }
    else if (a == 'E')
    {
        return 5;
    }
    else if (a == 'D')
    {
        return 7;
    }
    else if (a == 'C')
    {
        return 9;
    }
    else
    {
        return 0; //return 0 because compiler will not complete because need all possibilites of return to avoid freezing if input is different from other cases.
    }
}