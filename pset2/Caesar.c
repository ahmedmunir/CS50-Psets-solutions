// Implement a program that encrypts messages using Caesar’s cipher:
// $ ./caesar 13
// plaintext:  HELLO
// ciphertext: URYYB

//Code that cipher text depends on the key input from user.
#include <stdio.h>
#include <cs50.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

void convert_to_cipher(int key, string text); //this function will not return any thing
int main(int argc, string argv[])
{
    int key;
    string plaintext ;
    if (argc != 2)
    {
        printf("Your input must be program execution + key! NO MORE !!!!\n");
        return 1;
    }
    if (atoi(argv[1]) == 0) //check if the key which must be number contains any type else
    {
        printf("Error Key\n");
        return 1;
    }
    else
    {
        key = atoi(argv[1]) % 26; //this modulues to avoid entering number more than 26
        plaintext = get_string("paintext: \n");
        convert_to_cipher(key, plaintext);
    }
}

void convert_to_cipher(int key, string text)
{
    char ciphered[strlen(text)];
    int i = 0;
    while (i < strlen(text))
    {
        if (isalpha(text[i]))
        {
            if (isupper(text[i]))
            {
                int character_asci = (int) text[i] - 65; //convert character to ascii then to alpha index
                int ciphered_character = (character_asci + key) % 26; //apply equation provided
                char last_character = ciphered_character + 65; //do cipher & no need to convert integet to char
                ciphered[i] = last_character; //assign it to new string
            }
            else
            {
                int character_asci = (int) text[i] - 97; //convert character to ascii then to alpha index
                int ciphered_character = (character_asci + key) % 26; //apply equation provided
                char last_character = ciphered_character + 97; //do cipher
                ciphered[i] = last_character; //assign it to new string
            }
        }
        else
        {
            ciphered[i] = text[i];    //if it is not a character at all
        }
        i++;
    }
    printf("plaintext: %s\n", text);
    printf("ciphertext: %s\n", ciphered);
}
