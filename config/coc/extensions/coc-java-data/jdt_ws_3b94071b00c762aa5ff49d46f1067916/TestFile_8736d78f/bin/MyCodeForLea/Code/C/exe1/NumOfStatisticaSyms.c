#include <stdio.h>
#include <stdlib.h>

int main()
{
    int sn, tn, ln;
    sn = tn = ln = 0;
    
    int c;
    printf("Enter some text. Press Ctrl + D to stop.\n");

    while ((c = getchar()) != EOF)
    {
        if (c == ' ')
            sn++;
        if (c == '\t')
            tn++;
        if (c == '\n')
            ln++;
    }
    printf("输入的内容中有%d个空格符，%d个制表符，%d个换行符", sn, tn, ln);
    return 0;
}

