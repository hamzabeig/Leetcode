# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def itr_reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tmp = head
        prev = None
        curr = head
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        return prev
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # print(head)
        if head == None:
            return head

        if head.next== None:
            return head

        newhead = self.reverseList(head.next)
        # print(head)
        head.next.next = head
        head.next = None

        return newhead
        
        
        
        
        
        

        