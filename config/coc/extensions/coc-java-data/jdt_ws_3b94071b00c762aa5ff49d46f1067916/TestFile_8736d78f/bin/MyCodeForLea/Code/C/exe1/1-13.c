#include <stdio.h>

#define IN 1  // 在单词内
#define OUT 0 // 在单词外
#define MAX_LEN 20 // 最大单词长度

int main() {
    int c, state, len, i, j;
    int word_len[MAX_LEN]; // 统计单词长度的数组
    for(i = 0; i < MAX_LEN; i++) 
    {
        word_len[i] = 0; // 初始化为0
    }
    state = OUT; // 初始状态为在单词外
    len = 0;
    while((c = getchar()) != EOF)
    {
        if(c == ' ' || c == '\n' || c == '\t') 
        { // 如果是空白字符
            if(state == IN)
            { // 如果前一个字符是单词内的
                if(len <= MAX_LEN)
                { // 如果长度不超过最大值
                    ++word_len[len - 1]; // 统计长度
                } 
                else 
                {
                    ++word_len[MAX_LEN - 1]; // 超过最大值，归到最后一个
                }
            }
            state = OUT; // 切换到单词外状态
            len = 0; // 重置长度
        } 
        else 
        { // 非空白字符
            if(state == OUT)
            { // 如果前一个字符是单词外的
                state = IN; // 切换到单词内状态
            }
            ++len; // 增加长度
        }
    }
    printf("Length | Histogram\n");
    printf("-------------------\n");
    for(i = 0; i < MAX_LEN; i++) {
        printf("%6d | %d", i + 1, word_len[i] ); // 输出长度
        putchar('\n');
    }
    return 0;
}
