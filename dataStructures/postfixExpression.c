#include <stdio.h>
#include <malloc.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

struct stack {
  int top;
  int *arr;
};

struct stack* createStack(int len) {
  struct stack *stk;
  stk = malloc(sizeof(struct stack));

  stk->top = -1;

  stk->arr = (int*) malloc(len * sizeof(int));
  return stk;
}

int pop(struct stack *stack) {
  printf("pop:\t%d\n", stack->arr[stack->top]);
  return stack->arr[stack->top--];
}

void push(struct stack *stack, int i) {
  stack->arr[++stack->top] = i;
  printf("push:\t%d\n", stack->arr[stack->top]);
}

int calc(char * str)
{
  int len, i, val1, val2 = 0;
  struct stack *stk = NULL;

  if (str == NULL) return 0;
  len = strlen(str);
  if (len == 0) return 0;
  //printf("%d\n", len);

  stk = createStack(len);

  for (i = 0; i < len; i++) {
    //printf("\n%d", i);
    if (isdigit(str[i])){
      push(stk, str[i] - '0');
    }
    else {
      val2 = pop(stk);
      val1 = pop(stk);

      printf("%d %d\n", val1, val2);

      switch(str[i])
      {
        case '+':
          push(stk, val1+val2);
         break;
        case '-':
          push(stk, val1-val2);
          printf("stack top: %d\n", stk->top);
          break;
        case '/':
          push(stk, val1/val2);
          break;
        case '*':
          push(stk, val1*val2);
          break;
      }
    }
  }
  return pop(stk);
}

int main() {
  char * str;
  int val = 0;
  str = malloc(10);
  memset(str, 0, 10);
  strcpy(str, "123+*8-");

	val = calc(str);
  printf("%d", val);
	return 0;
}
