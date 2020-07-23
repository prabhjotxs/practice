#include "stdio.h"
#include "malloc.h"

int array[10];
void main()
{
  int i;
  for (i = 0; i < 10; i++)
    print("%d", array[i]);
}
