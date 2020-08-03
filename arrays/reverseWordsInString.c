#include <stdio.h>
#include <malloc.h>
#include <string.h>


int str_reverse(char** str, int start, int end) {
  char temp;

  //printf("start: %d, end: %d\n", start, end);

  while (start < end) {
    temp = (*str)[start];
    (*str)[start] = (*str)[end];
    (*str)[end] = temp;
    start++;
    end--;
  }

  //printf("reserve: X\n");
  return 0;
}

int main(void) {
  int len = 0;
  int start = 0;
  int end = 0;

  char *str = (char*) malloc(21);
  memset(str, 0, 21);
  strncpy(str, "I am Prabhjot Singh", 21);

  len = strlen(str);
  //printf("len: %d", len);
  str_reverse(&str, start, len-1);

  while (1) {
    if (start >= len) break;

    while (start < len && str[start] == ' ') {
      start++;
    }
    while (end < len && str[end] != ' ') {
      end++;
    }
    printf("start: %d, end: %d\n", start, end);
    str_reverse(&(str), start, end-1);


    end++;
    start = end-1;
  }

  printf("string: %s", str);
}
