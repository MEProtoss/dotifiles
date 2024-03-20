#include <stdio.h>

#define TABSIZE 8   // 定义制表符的大小（空格数）

int main()
{
    int c, pos;

    pos = 0;    // 初始化当前列的位置

    while ((c = getchar()) != EOF) 
    {
        if (c == '\t') 
        {  // 如果读到制表符，则输出适当数量的空格
            int nb = TABSIZE - (pos % TABSIZE);//计算需要输出多少个空格才能将列位置移动到下一个制表符终止位
            for (int i = 0; i < nb; ++i) 
            {
                putchar(' ');
                ++pos;
            }
        }
        else if (c == '\n')
        {  // 如果读到换行符，重置列位置
            putchar(c);
            pos = 0;
        } 
        else 
        {  // 否则输出字符并更新列位置
            putchar(c);
            ++pos;
        }
    }

    return 0;
}
