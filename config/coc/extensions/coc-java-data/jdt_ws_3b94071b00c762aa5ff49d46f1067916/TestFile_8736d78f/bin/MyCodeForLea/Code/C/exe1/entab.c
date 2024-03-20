#include <stdio.h>
#include <stdlib.h>
#define IN 1
#define OUT 0

int main()
{
    int c;
    int tn = 0, sn = 0;
    int state = OUT;
    int i;
    while ((c = getchar()) != EOF)
    {
        if (c == ' ')
        {
            state = IN;
            ++sn;//增加空格数量
        }
        else if (c == '\t' )
        {
            state = IN;//进入单词内部状态
            // 计算空格和制表符数量
            tn = sn / 4 + 1;
            sn = sn % 4;
            //打印空格和制表符
            for (i = 0 ; i < sn ; i++)
            {
                putchar(' ');
            }
            for (i = 0 ; i < tn; i++)
            {
                putchar('\t');
            }
            //重置sn和tn和状态
            sn = 0;
            tn = 0;
            state = OUT;
        }
        else
        {   
            // 计算空格和制表符数量
            tn = sn / 4 + 1;
            sn = sn % 4;
            //打印空格和制表符
            for (i = 0 ; i < sn ; i++)
            {
                putchar(' ');
            }
            for (i = 0 ; i < tn; i++)
            {
                putchar('\t');
            }
            // 打印当前字符 并重置
            putchar(c);
            state = OUT;
            sn = tn = 0;
        }
    }
}
