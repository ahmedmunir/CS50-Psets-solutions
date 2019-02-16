// Implement a program that encrypts messages using Vigenère’s cipher:
// $ ./vigenere ABC
// plaintext:  HELLO
// ciphertext: HFNLP

//this code to cipher a text depending on the key entered by user, this key must be string and doesnt have any number.
#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
void convert_to_cipher(string key, string text);
int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Please enter program execution command + one word\n");
        return 1; //we return 1 here because int main must return 0 if run successuflly but return1 will shut down the program.
    }
    else
    {
        int checker = 0;
        while (checker < strlen(argv[1]))
        {
            if (isalpha(argv[1][checker]) == false) //check for each character
            {
                printf("enter your key full of alphabet, dont include numbers, spaces etc\n");
                return 1;
            }
            checker++;
        }
        string key = argv[1];
        string plain_text = get_string("Enter your message to be encrypted: ");
        convert_to_cipher(key, plain_text);
    }
}

void convert_to_cipher(string key, string text)
{
    int key_checker = 0;
    int text_checker = 0;
    char ciphered[strlen(text)];
    ciphered[strlen(text)] = '\0'; //these 2 lines are very important to detect the end of index
    while (text_checker < strlen(text))
    {
        if (isalpha(text[text_checker]))
        {
            if (isupper(text[text_checker]))
            {
                int character_index = (int) text[text_checker] - 65; //convert character to ascii number then alphabet index
                if (isupper(key[key_checker % strlen(key)])) //this equation to keep inside loop of key word
                {
                    int key_number = (int) key[key_checker % strlen(key)] - 65; //convert key character to its number value at ascii
                    int ciphered_character = (character_index + key_number) % 26; //according to given equation
                    ciphered_character += 65;
                    ciphered[text_checker] = ciphered_character;
                    key_checker++;
                    text_checker++;
                }
                else //this case for lowercase characters and above one for upper case
                {
                    int key_number = (int) key[key_checker % strlen(key)] - 97;
                    int ciphered_character = (character_index + key_number) % 26;
                    ciphered_character += 65;
                    ciphered[text_checker] = ciphered_character;
                    key_checker++;
                    text_checker++;
                }
            }
            else //this case for character of message that is lowerCase
            {
                int character_index = (int) text[text_checker] - 97;
                if (isupper(key[key_checker % strlen(key)])) //this equation to keep inside loop of key word
                {
                    int key_number = (int) key[key_checker % strlen(key)] - 65; //convert key character to its number value at ascii
                    int ciphered_character = (character_index + key_number) % 26; //according to given equation
                    ciphered_character += 97;
                    ciphered[text_checker] = ciphered_character;
                    key_checker++;
                    text_checker++;
                }
                else //this case for lowercase characters and above one for upper case
                {
                    int key_number = (int) key[key_checker % strlen(key)] - 97;
                    int ciphered_character = (character_index + key_number) % 26;
                    ciphered_character += 97;
                    ciphered[text_checker] = ciphered_character;
                    key_checker++;
                    text_checker++;
                }
            }
        }
        else
        {
            ciphered[text_checker] = text[text_checker];
            text_checker++;
        }
    }
    printf("ciphertext: %s\n", ciphered);
}
