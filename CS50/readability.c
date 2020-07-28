#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

//int Count(string s, int letter, int word, int sentence);
int Count(string s);

int main(void)
{
    string s = get_string("Text: ");
    //Count(s, letter, word, sentence);
    int level = Count(s);
    printf("%i\n", level);
    if (level < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (level > 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", level);
    }
    

}

int Count(string s)
{
    int letter = 0, word = 0, sentence = 0;
    for (int i = 0, n = strlen(s); i <n; i++)
    {
        
        if (isalpha(s[i]))
        {
            letter += 1;
        }
        if (isspace(s[i]))
        {
            word += 1;
        }
        if (s[i] == '.' || s[i] == '?' || s[i] == '!')
        {
            sentence += 1;
        }
        
    }
    word += 1;
    printf("letter: %i word: %i sentence: %i\n", letter, word, sentence);
    float L = 0.0, S = 0.0;
    L = (float) letter / (float) word * 100;
    S = (float) sentence / (float) word * 100;

    return round(0.0588 * L - 0.296 * S - 15.8);
}