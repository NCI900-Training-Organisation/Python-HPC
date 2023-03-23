#include <stdlib.h>
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

