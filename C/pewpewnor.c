#include <malloc.h>
#include <stdio.h>
#include <string.h>

char *coffeeToCode(char *str) {
  const int N = strlen(str);

  for (int i = 0; i < N - 1; i++) {
    for (int j = 0; j < N - 1 - i; j++) {
      if (str[j] == 'C' || str[j] > str[j + 1]) {
        char temp = str[j];
        str[j] = str[j + 1];
        str[j + 1] = temp;
      }
    }
  }

  char *result = (char *)malloc(sizeof(char) * 4);
  int k = 0;

  for (int i = 0; i < N; i++) {
    if (i != N && str[i] == str[i + 1])
      continue;

    if (str[i] == 'f')
      result[k++] = 'd';
    else
      result[k++] = str[i];
  }
  result[4] = '\0';

  return result;
}

int main(void) {
  char sentence[] = "Coffee";
  char *result = coffeeToCode(sentence);

  for (int i = 4; i >= 0; i--) {
    printf("%c", result[i]);
  }
  printf("\n");

  free(result);

  return 0;
}
