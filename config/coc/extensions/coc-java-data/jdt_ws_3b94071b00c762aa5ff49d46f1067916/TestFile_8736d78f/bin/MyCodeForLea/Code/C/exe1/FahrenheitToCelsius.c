#include <stdio.h>
#include <stdlib.h>
// 当fahr =0, 20 , 40 ...，300时 ，打印华氏和摄氏的对照表

int main() {
    int fahr;
    int lower = 0;
    int upper = 300;
    int step = 20;

    printf("下面是华氏和摄氏的温度对照表\n");
    fahr = lower;

    for (fahr = upper; fahr >= lower; fahr = fahr - step)
        printf("%3d %6.1f\n", fahr, (5.0 / 9.0) * (fahr - 32));
}
