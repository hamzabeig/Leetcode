# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def itr_swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
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
    
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        self.newhead = head.next
        def swap(temp, curr):
            if not curr or not curr.next:
                return curr
            
            curr1 = curr
            curr2 = curr.next
            
            curr1.next = curr2.next
            curr2.next = curr1
            if temp != curr1:
                temp.next = curr2
            swap(curr1, curr1.next)
            return self.newhead
        return swap (head, head)
