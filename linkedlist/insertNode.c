#include <stdio.h>
#include <malloc.h>

typedef struct n{
  int value;
  struct n* next;
} node;

//node* head = NULL;
#define NEWNODE malloc(sizeof(node))

void insertnode(node** head, int value, int pos)
{
  int i = 0;
  node* temp = *head;
  node* newnode;

  //empty list, create head
  if (*head == NULL) {
    *head = NEWNODE;
    (*head)->value = value;
    (*head)->next = NULL;
    return;
  }

  //allocate new node and wait to insert at right pos
  newnode = NEWNODE;
  newnode->value = value;

  //if need change head
  if (pos == 0) {
    newnode->next = *head;
    *head = newnode;
    return;
  }

  //traverse to the end or to the position
  for (i = 0 ; temp->next != NULL && i < pos-1 ; i++)
    temp = temp->next;

  //if position is before end
  if (temp->next != NULL) {
    newnode->next = temp->next;
    temp->next = newnode;
  }
  //if position after the end
  else {
    newnode->next = NULL;
    temp->next = newnode;
  }
}

void reverseList(node** head) {
  node* prev = NULL;
  node* curr = *head;
  node* next = NULL;

  for (;curr != NULL;) {
    next = curr->next;
    curr->next = prev;
    prev = curr;
    curr = next;
  }
  *head = prev;
}

void printList(node** head)
{
  node* temp = *head;

  for (;temp->next != NULL;) {
    printf("%d\n", temp->value);
    temp = temp->next;
  }
  printf("%d\n", temp->value);
}

int main(void) {
  node* head = NULL;

  insertnode(&head, 50, 0);
  insertnode(&head, 51, 0);
  insertnode(&head, 52, 0);
  insertnode(&head, 53, 0);
  insertnode(&head, 54, 0);
  insertnode(&head, 55, 0);
  insertnode(&head, 56, 0);
  insertnode(&head, 57, 0);
  insertnode(&head, 40, 0);
  insertnode(&head, 30, 1);
  insertnode(&head, 20, 100);

  printList(&head);
  reverseList(&head);
  printf("\nReversedList\n");
  printList(&head);
  return 0;
}
