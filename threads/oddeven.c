#include <stdio.h>
#include <pthread.h>

int count = 0;
pthread_mutex_t lock = PTHREAD_MUTEX_INITIALIZER;
pthread_cond_t condition = PTHREAD_COND_INITIALIZER;

void* thread_proc1(void* arg)
{
  pthread_mutex_lock(&lock);
  while(1)
  {
    if (count >10)
    {
      pthread_mutex_unlock(&lock);
      break;
    }
    if (count%2 == 1)
    {
      printf("odd: \t%d\n", count);
      count++;
    }
    else
    {
      pthread_cond_signal(&condition);
      pthread_mutex_unlock(&lock);
    }
  }
  return NULL;
}

void* thread_proc2(void *arg)
{
  pthread_mutex_lock(&lock);
  while(1)
  {
    if (count >10)
    {
      pthread_mutex_unlock(&lock);
      break;
    }
    if (count%2 == 0)
    {
      printf("even: \t%d\n", count);
      count++;
    }
    else
    {
      pthread_cond_signal(&condition);
      pthread_mutex_unlock(&lock);
    }
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

  return 0;
}
