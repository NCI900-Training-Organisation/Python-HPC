#include <stdlib.h>
#include <iostream>
#include "pi.h"

int sample(void)
{
    double x = ((double) rand()) / (RAND_MAX);
    double y = ((double) rand()) / (RAND_MAX);

    if ((x*x + y*y) <= 1)
    {
        return 1;
    }
    return 0;
}


int sample_serial(int nsamples)
{
    int count = 0;
    for(int i = 0; i <= nsamples; i++)
    {
        count += sample();
    }
    return count;
}

