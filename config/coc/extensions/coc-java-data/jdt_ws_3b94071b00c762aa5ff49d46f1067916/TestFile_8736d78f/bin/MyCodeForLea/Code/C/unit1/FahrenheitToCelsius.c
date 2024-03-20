#include <stdio.h>
#include <stdlib.h>
// 当fahr =0, 20 , 40 ...，300时 ，打印华氏和摄氏的对照表

main()
{
    float fahr, celsius;
    int lower = 0;
    int upper = 300;
    int step = 20;

    printf("下面是华氏和摄氏的温度对照表");
    fahr = lower;
    while (fahr <= upper)
    {
        // celsius = (5/9)*(fahr-32); 
        celsius = 5 * (fahr - 32) / 9;
        printf("%3.0f %6.1f\n", fahr, celsius);
        fahr = fahr + step;
    }
}


