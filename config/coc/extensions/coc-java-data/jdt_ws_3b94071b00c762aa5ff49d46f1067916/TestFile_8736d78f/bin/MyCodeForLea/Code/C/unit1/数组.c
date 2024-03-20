#include <stdio.h>
#include <stdlib.h>

// 统计各个数字，空白符及其他字符出现的次数

main()
{
    int c;
    int i;
    int n_num, n_white, n_other = 0;
    int ndight[10];
    for (i = 0;i <= 10; ++i)
        ndight[i] = 0;

    while ((c = getchar()) != EOF)
        if (c >= '0' && c <='9')
            ndight[c-'0'] = ndight[c-'0'] + 1;
        else if (c == ' ' || c == '\n' || c == '\t')
            ++n_white;
        else
            ++n_other;

    printf("digits = ");
    for (i = 0; i < 10; ++i)
        printf("%d", ndight[i]);
    printf(", white space = %d, other = %d\n",n_white, n_other);
}
