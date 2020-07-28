#include <cs50.h>
#include <stdio.h>

// const int N = 3;

float average(int length, int array[])

int main(void)
{
    // Get number of scores
    int n = get_int("Scores: ")

    // Scores
    int scores[n];
    for (int i = 0; i < n; i++)
    {
        scores[i] = get_int("Score %i: ", i + 1)
    }

    // Print average
    printf("Average: %.2f\n", average(n, scores));
}

float average(int length, int array[])
{
    int sum = 0;
    for (int i = 0; i < length; i++)
    {
        sum += array[i];
    }
    return (float) sum / (float) length;
}