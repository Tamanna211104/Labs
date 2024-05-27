                //C tutorial//


// https://www.youtube.com/watch?v=87SH2Cn0s9A reference video
/*
1. C is not an object oriented language
it is procedural not abstract
2. C++ is Object oriented extension of C

Necessities :
IDE (integrated development enviroment) : Text editor basicaally VS code
GCC (GNU Compiler Collection) Compiler : optimizing compiler produced by the GNU Project supporting various programming languages, hardware architectures and operating systems
it simply converts C code to machine code

in extensions install C/C++ and Code Runner
*/

/*
explaining basic syntax in C
#inlude : a pre processor command that tells the complier to include the contents of a file
<stdio.h> : the file we would like to include (std = standard) (io = input output)
entry point of our code is the main function type :
int main() {
    anything within this set of curly braces is within the main function

    To display something :

    printf("working sucks");

    to add another statement repeat this step

    printf("Minimum wage needs to be more than $14.2");

    the output will be displayed as :
    working sucks Minimum wage needs to be more than $14.2

    since this is one very long line of text to shift second statement to next line :
    add an escape sequence for a new line character \n

    printf("working sucks\n");
    printf("Minimum wage needs to be more than $14.2\n")

    output will be:
    working sucks
    Minimum wage needs to be more than $14.2

    It won't adjust minimum wage to inflation but it looks neat

    add retun statement at the end  of every function
    this will return the exit status of our program
    we return a zero if our program runs successfully
    if no errors 0 will be return
    if there r errors 1 will be returned
    the semicolon is used to terminate statements similar to a period after a sentence

    return 0;
}
*/
#include <stdio.h>

int main()
{
    printf("Hello World\n");
    return 0;
}

