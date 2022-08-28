/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    void reorderList(ListNode* head) {
        // VERY interesting
        // step 1: find middle of list
        //      have a fast pointer (iterate by 2) and slow pointer (iterate by 1)
        //      when fast pointer reaches the end, slow pointer will be at the middle
        // step 2: reverse the second half
        // step 3: reorder the list by interchanging between first half and second half
        
        if (head == NULL || head->next == NULL) return;
        
        // find middle
        ListNode* fast = head;
        ListNode* slow = head;
        while (fast->next && fast->next->next) {
            fast = fast->next->next;
            slow = slow->next;
        }
        
        // reverse list starting at slow+1 (middle+1)
        ListNode* front = slow;
        ListNode* afterFront = front->next;
                
        while (afterFront->next) {
            ListNode* twoAfterFront = afterFront->next;
            afterFront->next = twoAfterFront->next;
            twoAfterFront->next = front->next;
            front->next = twoAfterFront;
        }
        
        
        // reordering list
        ListNode *headCopy = head;
        ListNode *mid = slow->next;
        while (headCopy != slow && mid) {
            slow->next = mid->next;
            mid->next = headCopy->next;
            headCopy->next = mid;
            headCopy = mid->next;
            mid = slow->next;
        }
    }
};
