#include <stdio.h>
#include <stdlib.h>
// Declaring or defining the nodes as struct
struct ListNode{
    int val;
    struct ListNode* next;
};

// creating a node, allocating dynamic memory and values to it
struct ListNode* createNode(int ele){
    struct ListNode* newNode = (struct ListNode*)malloc(sizeof(struct ListNode));
    newNode->val = ele;
    newNode->next = NULL;
    return newNode;
}
struct ListNode* insetAtFront(struct ListNode* head, int ele){
  struct ListNode* newNode = createNode(ele);
  newNode->next = head;
  return newNode;
}
void main(){

    struct ListNode* head = createNode(20);
    head->next = createNode(30);
    head->next->next = createNode(40);
    head->next->next = createNode(50);

    head = insetAtFront(head,10);
    printList(head);

}

