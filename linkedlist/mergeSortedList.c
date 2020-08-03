#include <stdio.h>
#include <malloc.h>

typedef struct node {
  int data;
  struct node* next;
} NODE;

NODE* head1 = NULL;
NODE* head2 = NULL;
NODE* ml = NULL;

int insertNode(NODE** head, int data) {
  struct node* temp;
  struct node* newNode;
  //printf("head:%p\n", *head);
  if (*head == NULL) {
    *head = malloc(sizeof(NODE));
    (*head)->data = data;
    (*head)->next = NULL;
    return 0;
  }

  temp = *head;
  while (temp->next != NULL) {
    temp = temp->next;
  }

  newNode = malloc(sizeof(NODE));
  newNode->data = data;
  newNode->next = NULL;
  temp->next = newNode;

  return 0;
}

int mergeList(NODE** ml_head, NODE* head1, NODE* head2) {
  NODE* h1;
  NODE* h2;
  NODE* ml_tail;

  h1 = head1;
  h2 = head2;

  if (h1 == NULL) {
    *ml_head = h2;
    return 0;
  }
  else if (h2 == NULL) {
    *ml_head = h1;
    return 0;
  }

  *ml_head = malloc(sizeof(NODE));
  //check memory fail
  ml_tail = *ml_head;

  //can make a separate function for this to avoid repeating
  if (h1->data < h2->data) {
    (*ml_head)->data = h1->data;
    h1 = h1->next;
  }
  else {
    (*ml_head)->data = h2->data;
    h2 = h2->next;
  }

  while (h1 != NULL && h2 != NULL) {
    ml_tail->next = malloc(sizeof(NODE));
    if (h1->data < h2->data) {
      ml_tail->next->data = h1->data;
      h1 = h1->next;
    }
    else {
      ml_tail->next->data = h2->data;
      h2 = h2->next;
    }
    ml_tail = ml_tail->next;
  }

  if (h1 != NULL)
    ml_tail->next = h1;
  else if (h2 != NULL)
    ml_tail->next = h2;

  return 0;
}

void printList(NODE* head) {
  NODE* temp;
  if (head == NULL) {
    printf("Empty list!");
  }

  temp = head;
  while (temp) {
    printf("%d\n", temp->data);
    temp = temp->next;
  }
}

int main(void) {
  insertNode(&head1, 5);
  insertNode(&head1, 7);
  insertNode(&head1, 9);

  insertNode(&head2, 6);
  insertNode(&head2, 8);
  insertNode(&head2, 10);
  insertNode(&head2, 12);
  insertNode(&head2, 14);

  printList(head1);
  printf("\n");
  printList(head2);
  printf("\n");

  mergeList(&ml, head1, head2);

  printList(ml);

  return 0;
}
