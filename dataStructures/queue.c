#include <stdio.h>
#include <malloc.h>
#include <string.h>

typedef struct q {
  int read;
  int write;
  int* arr;
} QUEUE;

typedef QUEUE* PQUEUE;

#define MAX_QUEUE 10

int enqueue(PQUEUE* q, int val) {
  if (((*q)->write % MAX_QUEUE == (*q)->read % MAX_QUEUE) &&
     ((*q)->arr[(*q)->write] != 0)) {
    printf("MAX queue reached!\n");
    return -1;
  }
  printf("enqueued!\n");
  (*q)->arr[(*q)->write++] = val;
  return 0;
}

int dequeue(PQUEUE* q) {
  int t;
  if ((*q)->write == 0) {
    printf("Nothng to read!\n");
    return -1;
  }
  t = (*q)->arr[(*q)->read];
  (*q)->arr[(*q)->read++] = 0;
  return t;
}

int clear(QUEUE* s) {
  return 0;
}

int size(PQUEUE* q) {
  return (*q)->write - (*q)->read;
}

int main(void) {
  PQUEUE q;
  q = malloc(sizeof(QUEUE));
  q->read = 0;
  q->write = 0;
  q->arr = malloc(sizeof(int) * MAX_QUEUE);
  memset(q->arr, 0, MAX_QUEUE);

  enqueue(&q, 5);
  enqueue(&q, 9);
  enqueue(&q, 11);
  enqueue(&q, 13);
  enqueue(&q, 15);
  enqueue(&q, 15);
  enqueue(&q, 15);
  enqueue(&q, 15);
  enqueue(&q, 15);
  enqueue(&q, 15);
  enqueue(&q, 15);
  //dequeue(&q);
  //enqueue(&q, 15);
  //dequeue(&q);
  //size(&q);
  //clear(&q);
  printf("dequeue: %d\n", dequeue(&q));
  printf("size %d\n", size(&q));
  return 0;
}
