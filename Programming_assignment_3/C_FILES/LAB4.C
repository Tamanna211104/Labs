#include <stdio.h>
int x = 10;
int main()
{
    printf("x is at location %p\n", &x);
}
#include <stdio.h>
int main()
{
    // define 5 arrays of different types
    int a[10];
    float b[10];
    double c[10];
    long d[10];
    char e[10];

    printf("Addresses A %p %p\n", &a[1], &a[0]);
    printf("Addresses B %p %p\n", &b[1], &b[0]);
    printf("Addresses C %p %p\n", &c[1], &c[0]);
    printf("Addresses D %p %p\n", &d[1], &d[0]);
    printf("Addresses E %p %p\n", &e[1], &e[0]);
}



#include <stdio.h>

typedef struct
{
    int a;
    int b;
} int_struct;

typedef struct
{
    int a;
    char b;
} mixed_struct;

int main()
{
    int_struct a[10];
    mixed_struct b[10];

    printf("Addresses A %p %p\n", &a[1], &a[0]);
    printf("Addresses B %p %p\n", &b[1], &b[0]);
}

#include <stdio.h>

int main()
{
    char c;
    for(c = 'A';c <= 'Z'; c = c+1)
    {
        printf("Character %c: %d decimal | 0x%x hex\n", c, c, c);
    }
}
