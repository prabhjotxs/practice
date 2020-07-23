#include <stdio.h>
#include <string.h>

int main()
{
  int maxl = 0;
  int maxr = 0;
  int left = 0;
  int rght = 3;
  int result = 0;
  int arr[] = {6, 9, 9};//{7, 4, 0, 9};//{3, 0, 0, 2, 0, 4};

  while (left <= rght) {
    if (arr[left] < arr[rght]) {
      if (arr[left] > maxl) {
        maxl = arr[left];
      }
      else {
        result += maxl - arr[left];
      }
      left++;
    }
    else {
      if (arr[rght] > maxr) {
        maxr = arr[rght];
      }
      else {
        result += maxr - arr[rght];
      }
      rght--;
    }
  }

  printf("result: %d\n", result);
  return 0;
}
