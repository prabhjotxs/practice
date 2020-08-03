#include <stdio.h>
#include <malloc.h>

typedef struct stk {
  int top;
  int* arr;
} STACK;

#define MAX_STACK 10

int push(STACK** s, int val) {
  if ((*s)->top == MAX_STACK) {
    printf("MAX limit reached!\n");
    return -1;
  }

  (*s)->arr[(*s)->top++] = val;
  return 0;
}

int pop(STACK** s) {
  if ((*s)->top == 0) {
    printf("Stack empty!!\n");
    return -1;
  }
  return (*s)->arr[--(*s)->top];
}

int clear(STACK** s) {
  if ((*s)->top == 0)
    return 0;

  while ((*s)->top > 0)
    pop(s);

  return 0;
}

int main(void) {
  STACK* s;
  s = malloc(sizeof(STACK));
  s->top = 0;
  s->arr = malloc(sizeof(int) * MAX_STACK);

  push(&s, 7);
  push(&s, 9);
  push(&s, 11);
  push(&s, 13);
  push(&s, 13);
  push(&s, 13);
  push(&s, 13);
  push(&s, 13);
  push(&s, 13);
  push(&s, 13);
  push(&s, 13);

  pop(&s);
  pop(&s);
  clear(&s);

  printf("stack top: %d", pop(&s));
  return 0;
}
