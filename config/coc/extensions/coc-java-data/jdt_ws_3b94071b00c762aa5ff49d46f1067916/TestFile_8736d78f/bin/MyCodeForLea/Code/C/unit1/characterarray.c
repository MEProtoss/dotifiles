#include <stdio.h>
#include <stdlib.h>
// 允许输入的最大长度
#defien MAXLINE 1000 
int max ;
char line[MAXLINE];
char longest[MAXLINE];

int getline(void);
void copy(void);

// 打印最长的行

main()
{
  int len; 
  extern int max;
  extern char longest[];

  max = 0;
  while ((len = getline(line,MAXLINE)) > 0)
      if (len > max)
      {
          max = len;
          copy(longest, line);
      }
  if (max > 0 ) /*存在这样的行*/
      printf("%s", longest);
  return 0;
}

/* 
 *  (special version)getline函数： 将一行读入s中并返回其长度
 */
int getline(void)
{
    int c, i;

    for (i = 0, i < MAXLINE-1 && (c=getchar()) != EOF && c!='\n'; ++i) /*逐字读入字符数组*/
        line[i] = c;
    if (c == '\n')
    {
        line[i] = c;
        ++i;
    }
    line[i] == '\0';
    return i;
}

/* (special version)copy函数：将form复制到to;这里假设to足够大 */
void copy(void)
{
    int i;
    extern char line[], longest[];

    i = 0;
    while ((to[i] = from[i]) != '\0')
        ++i;
}
