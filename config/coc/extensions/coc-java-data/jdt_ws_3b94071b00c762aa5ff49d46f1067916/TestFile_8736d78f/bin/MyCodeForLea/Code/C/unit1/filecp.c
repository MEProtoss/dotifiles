#include <stdio.h>
#include <stdlib.h>

int main(void) {
  printf("Please enter a character:\n");
  int result = getchar() != EOF;
  printf("The value of the expression getchar() != EOF is: %d\n", result);
  return 0;
}
