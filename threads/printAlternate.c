#include <stdio.h>
#include <pthread.h>

int count = 0;
pthread_mutex_t lock = PTHREAD_MUTEX_INITIALIZER;
pthread_cond_t condition1 = PTHREAD_COND_INITIALIZER;
pthread_cond_t condition2 = PTHREAD_COND_INITIALIZER;

void* thread_proc1(void* arg)
{
  while(1)
  {
    pthread_mutex_lock(&lock);

    if (count > 10)
    {
      pthread_cond_signal(&condition2);
      pthread_mutex_unlock(&lock);
      break;
    }

    printf("thread proc 1: count: %d\n", count);
    count++;

    pthread_cond_signal(&condition2);
    pthread_cond_wait(&condition1, &lock);
    pthread_mutex_unlock(&lock);
  }
  return NULL;
}

void* thread_proc2(void* arg)
{
  while(1)
  {
    pthread_mutex_lock(&lock);

    if (count > 10)
    {
      pthread_cond_signal(&condition1);
      pthread_mutex_unlock(&lock);
      break;
    }

    printf("thread proc 2: count: %d\n", count);
    count++;

    pthread_cond_signal(&condition1);
    pthread_cond_wait(&condition2, &lock);
    pthread_mutex_unlock(&lock);
  }
  return NULL;
}

int main(void) {
  pthread_t thread_id1;
  pthread_t thread_id2;

  pthread_create(&thread_id1, NULL, thread_proc1, NULL);
  pthread_create(&thread_id2, NULL, thread_proc2, NULL);
  pthread_join(thread_id1, NULL);
  pthread_join(thread_id2, NULL);
  printf("Hello Guransh\n");

  pthread_mutex_destroy(&lock);
  pthread_cond_destroy(&condition1);
  pthread_cond_destroy(&condition2);

  printf("resource destroyed");

  return 0;
}
