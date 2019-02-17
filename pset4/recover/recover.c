/****************************************************************************
 * recover.c
 *
 * Computer Science 50
 * Problem Set 4
 *
 * Recovers JPEGs from a forensic image.
 ***************************************************************************/

#include <stdio.h>
#include <stdint.h>

const int BLOCK_SIZE = 512;

int main(int argc, char *agrv[])
{
    FILE *f;

    if ((f = fopen(agrv[1], "r")) == NULL)
    {
        printf("Error opening the file \"ecard.raw\"...");
        return 1;
    }

    if (argc != 2)
    {
        fprintf(stderr, "enter command line + name of file\n");
        return 2;
    }

    uint8_t buf[512];

    int counter = 0;
    FILE *fw = NULL;

    // Iterate over file contents and if we coudlnt read full 512 bytes it will be false and that means we reach the end of file
    while (fread(buf, BLOCK_SIZE, 1, f))
    {
        // Check if the first four bytes are a JPEG signature
        if (buf[0] == 0xff && buf[1] == 0xd8 && buf[2] == 0xff
            && (buf[3] == 0xe0 || buf[3] == 0xe1))
        {
            // Close the file, if it is opened
            if (fw != NULL)
            {
                fclose(fw);
            }
            //every time we create new file that will take new space inside ram
            char filename[8];
            sprintf(filename, "%03d.jpg", counter);

            // Open a new JPEG file for writing
            fw = fopen(filename, "w");

            counter++;
        }

        if (fw != NULL)
        {
            fwrite(buf, BLOCK_SIZE, 1, fw);
        }
    }
    //closing the file after recover is done
    if (fw != NULL)
    {
        fclose(fw);
    }
    fclose(f);

    return 0;
}