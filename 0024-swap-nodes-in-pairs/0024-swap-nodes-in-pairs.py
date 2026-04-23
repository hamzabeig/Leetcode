# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head

        temp = head
        c1 = head
        c2 = head.next
        head = c2

        while c1 and c2:
            c1.next = c2.next
            c2.next = c1

            temp = c1
            
            c1 = c1.next
            if c1 is None:
                break
            c2 = c1.next
            if c2 is None:
                break
            temp.next = c2

        return head
        