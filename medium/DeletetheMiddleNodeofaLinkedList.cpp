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
    ListNode* deleteMiddle(ListNode* head) {
        // find midder using fast & slow approach
        // keep track of prev and next
        
        if (head->next == NULL) {
            delete head;
            return NULL;
        }
        
        ListNode *fast = head;
        ListNode *slow = head;
        ListNode *prev = NULL;
        
        while (fast->next && fast->next->next) {
            prev = slow;
            slow = slow->next;
            fast = fast->next->next;
        }
        
        if (fast->next) {
            // even
            prev = slow->next->next;
            delete slow->next;
            slow->next = prev;
        } else {
            // odd
            prev->next = slow->next;
            delete slow;
        }
                
        return head;
    }
};
