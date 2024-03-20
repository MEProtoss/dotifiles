// 将字符串t连接到字符串s的尾部；s必须有足够大的空间
1.先找s的尾部的位置；
2.再将t逐位复制
void struct(char s[], char t[])
{
    int i, j;

    i = j = 0;
    while (s[i] != '\0')
    {
        i ++;
    }
    while (s[i++] == t[j++] != '\0') // copy t
        ;
}
