#include <iostream>

using namespace std;

// Definition for singly-linked list.
struct ListNode
{
    int val;
    ListNode *next;
    // it's a contructor, which uses initialization list.
    // https://en.cppreference.com/w/cpp/language/initializer_list
    ListNode(int x) : val(x), next(NULL) {}
};

// iterative solution
// time complexity O(n), space complexity O(1)
class SolutionIT
{
public:
    ListNode *reverseList(ListNode *head)
    {
        if (!head)
        {
            return nullptr;
        }
        // set prev pointer to NULL
        // 头节点
        ListNode *prev = NULL;
        // set curr pointer to head
        // 第一个节点
        ListNode *curr = head;
        while (curr != NULL)
        {
            // temporarily store curr pointer to next
            // 暂存第一个节点指向下一个的指针
            ListNode *nextTemp = curr->next;
            // reverse pointer, move the next of curr node as prev
            curr->next = prev;
            // move backward
            prev = curr;
            curr = nextTemp;
        }
        // curr is pointer to NULL, prev is pointer to last node(new head)
        return prev;
    }
};

// recursive solution
// time complexity O(n), space complexity O(n)
class SolutionRE
{
public:
    ListNode *reverseList(ListNode *head)
    {
        if (head == NULL || head->next == NULL)
            return head;
        ListNode *curr = reverseList(head->next);
        head->next->next = head;
        head->next = NULL;
        return curr;
    }
};

// driver code

void printNode(ListNode *head)
{
    while (head != NULL)
    {
        cout << head->val << "->";
        head = head->next;
    }
    if (head == NULL)
        cout << "NULL";
}

int main()
{
    ListNode *node1 = new ListNode(1);
    ListNode *node2 = new ListNode(2);
    ListNode *node3 = new ListNode(3);
    ListNode *node4 = new ListNode(4);
    ListNode *node5 = new ListNode(5);
    node1->next = node2;
    node2->next = node3;
    node3->next = node4;
    node4->next = node5;
    node5->next = NULL;

    cout << "Given linked list\n";
    printNode(node1);

    SolutionIT solit;
    ListNode *prev = solit.reverseList(node1);

    cout << "\nReversed Linked list \n";
    printNode(prev);

    return 0;
}