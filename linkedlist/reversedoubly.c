#include <stdio.h>
#include <string.h>
#include <malloc.h>

typedef struct n {
  char* value;
  struct n* prev;
  struct n* next;
} node;

#define NEWNODE malloc(sizeof(node))

void insertNode(node** head, char* str) {
  node* temp = *head;
  node* newnode = NULL;

  if (*head == NULL) {
    *head = NEWNODE;
    (*head)->value = malloc(strlen(str));
    strncpy((*head)->value, str, strlen(str));
    (*head)->prev = NULL;
    (*head)->next = NULL;
    return;
  }

  for (;temp->next != NULL;) {
    temp = temp->next;
  }

  newnode = NEWNODE;
  newnode->value = malloc(strlen(str));
  strncpy(newnode->value, str, strlen(str));
  newnode->next = NULL;
  newnode->prev = temp;
  temp->next = newnode;
}

void reverselist(node** head) {
  node* temp = NULL;
  node* prev = NULL;
  node* curr = *head;

  for (;curr != NULL;) {
    temp = curr->next;
    curr->prev = curr->next;
    curr->next = prev;
    prev = curr;
    curr = temp;
  }
  *head = prev;
}

void printlist(node** head) {
  node* t = *head;

  for (;t->next != NULL;) {
    printf("%s\n", t->value);
    t = t->next;
  }
  printf("%s\n", t->value);
}

int main(void) {
  node* head = NULL;

  insertNode(&head, "amit");
  insertNode(&head, "arun");
  insertNode(&head, "annu");
  printlist(&head);
  printf("\nreversed list\n");
  reverselist(&head);
  printlist(&head);
  return 0;
}
