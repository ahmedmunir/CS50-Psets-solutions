// Implements a dictionary's functionality
//this code will save more memory but slower

#include <stdbool.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "dictionary.h"

//declare hash function
int hash_function(char *x);

//create structure of nodes to make linked list of data structure
typedef struct node
{
    char word[LENGTH + 1]; //length of word will not exceed 45 and +1 for /0
    struct node *next;
}
node;

//make 26 hashtable elements to construct hashtable
node *hashtable[60000];

//declare variable size to store number of words inside dictionary
unsigned int words_in_dict = 0;

// Returns true if word is in dictionary else false
bool check(const char *word)
{
    // TODO
    char word_checker[LENGTH + 1];
    int len = strlen(word);
    //change the word to be all lowercase
    for (int i = 0 ; i < len; i++)
    {
        word_checker[i] = tolower(word[i]);
    }
    word_checker[len] = '\0';

    //get the index of hastable
    int x = hash_function(word_checker);

    //make temporary pointer to loop through linked list to check about the word
    node *tmp = hashtable[x];
    while (tmp != NULL)
    {

        //check whether the word is exist in linked list or not
        if (strcmp(tmp -> word, word_checker) == 0)
        {
            return true;
        }
        else
        {
            tmp = tmp -> next;
        }
    }
    return false;
}

// Loads dictionary into memory, returning true if successful else false
bool load(const char *dictionary)
{
    // TODO
    //open the dictionary file
    FILE *file = fopen(dictionary, "r");

    //create a word of length 46
    char word_looper[LENGTH + 1];

    //making all pointers of 26 structures points to NULL at initialization
    for (int k = 0; k < 26; k++)
    {
        hashtable[k] = NULL;
    }

    //to check whether we start to store elements
    bool enter = false;

    //index through word_looper
    int word_looper_index = 0;

    //scanning for all words inside dictionary
    for (char c = fgetc(file); c != EOF; c = fgetc(file))
    {
        //storing characters inside word_looper
        if (c != '\n')
        {
            if (isalpha(c))
            {
                c = tolower(c);
                word_looper[word_looper_index] = c;
                word_looper_index ++;
            }
            else
            {
                word_looper[word_looper_index] = c;
                word_looper_index ++;
            }
        }
        else
        {
            word_looper[word_looper_index] = '\0';
            word_looper_index = 0;
            enter = true;
        }

        if (enter == true)
        {
            //getting the index of that word
            int index_of_element = hash_function(word_looper);

            //check whether it is the first element of linked list or not
            if (hashtable[index_of_element] == NULL)
            {
                node *node1 = malloc(sizeof(node));
                //check if we run out of memory
                if (node1 == NULL)
                {
                    unload();
                    return false;
                    words_in_dict = 0;
                }
                else
                {
                    hashtable[index_of_element] = node1;
                    node1 -> next = NULL;
                    strcpy(node1 -> word, word_looper);
                    words_in_dict ++;
                }
            }
            else
            {
                //assign the head to tmp to use it for checking
                node *tmp = hashtable[index_of_element];
                //to check whether the word is found or not
                bool found = false;
                while (tmp != NULL)
                {
                    //if word was already in linked list
                    if (strcmp(tmp -> word, word_looper) == 0)
                    {
                        found = true;
                        break;
                        words_in_dict ++;
                    }
                    else
                    {
                        tmp = tmp -> next;
                    }
                }
                //if the word is new and never exist
                if (found == false)
                {
                    node *node2 = malloc(sizeof(node));
                    if (node2 == NULL)
                    {
                        unload();
                        return false;
                        words_in_dict = 0;
                    }
                    //assign the word_looper array to node2 word
                    strcpy(node2 -> word, word_looper);
                    node2 -> next = hashtable[index_of_element];
                    hashtable[index_of_element] = node2;
                    words_in_dict ++;
                }
            }
        }
        enter = false;
        // free(word_looper);
    }
    fclose(file);
    return true;
}

// Returns number of words in dictionary if loaded else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    if (words_in_dict == 0)
    {
        return 0;
    }
    else
    {
        return words_in_dict;
    }
}

// Unloads dictionary from memory, returning true if successful else false
bool unload(void)
{
    // TODO
    for (int looper = 0; looper < 60000; looper++)
    {
        node *tmp = hashtable[looper];
        while (hashtable[looper] != NULL)
        {
            tmp = tmp -> next;
            free(hashtable[looper]);
            hashtable[looper] = tmp;
        }
    }
    return true;
}

//creation of hash function
int hash_function(char *x)
{
    int sum = 0;
    //converting the whole word to become lowercase for insensitive case
    for (int i = 0; x[i] != '\0'; i++)
    {
        sum += x[i];
    }
    return sum % 60000;
}