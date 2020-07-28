// get key
// check key: len, non alphabetic, no duplication
// get plaintext, get_string
// encipher
// print ciphertext

#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }

    string s = argv[1];
    //char *lowercase = malloc(26 * sizeof(char));
    //char *uppercase = malloc(26 * sizeof(char));
    char lowercase[26];
    char uppercase[26];
    // printf("lowercase%s\n", lowercase);

    for (int i = 0, n = strlen(s); i < n; i++)
    {
        if (isalpha(s[i]))
        {
            if (s[i] >= 'a' && s[i] <= 'z')
            {
                for (int j = 0, m = strlen(lowercase); j < m; j++)
                {
                    if (lowercase[j] == s[i])
                    {
                        printf("Key must not contain repeated characters\n");
                        return 1;
                    }
                }
                lowercase[i] = s[i];
                uppercase[i] = toupper(s[i]);
            }
            else
            {
                for (int j = 0, m = strlen(lowercase); j < m; j++)
                {
                    if (lowercase[j] == tolower(s[i]))
                    {
                        printf("Key must not contain repeated characters\n");
                        return 1;
                    }
                }
                lowercase[i] = tolower(s[i]);
                uppercase[i] = s[i];
            }
        }
        else
        {
            printf("Usage: ./substitution key\n");
            return 1;
        }
    }


    if (strlen(s) != 26)
    {
        printf("Key must contain 26 characters.\n");
        return 1;
    }

    string plaintext = get_string("plaintext:");

    char *output = malloc(strlen(plaintext) * sizeof(char));
    char key1[26] = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'};
    char key2[26] = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'};
    for (int x = 0, n = strlen(plaintext); x < n; x++)
    {
        if (plaintext[x] >= 'a' && plaintext[x] <= 'z')
        {
            for (int y = 0; y < 26; y++)
            {
                if (plaintext[x] == key2[y])
                {
                    output[x] = lowercase[y];
                    // printf("%c\n", lowercase[y]);
                    // printf("2 %s\n", output);
                    break;
                }
            }

        }
        else if (plaintext[x] >= 'A' && plaintext[x] <= 'Z')
        {
            for (int y = 0; y < 26; y++)
            {
                if (plaintext[x] == key1[y])
                {
                    output[x] = uppercase[y];
                    // printf("3 %s\n", output);
                    break;
                }
            }
        }
        else
        {
            output[x] = plaintext[x];
        }
    }
    printf("ciphertext: %s\n", output);
    free(output);
    return 0;

}
