# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    tmp = odd.next
    odd.next = even.next
    even.next = even.next.next
    odd.next.next = tmp
    odd = odd.next
    even = even.next

    -------------------------------------------------
    1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None
    odd = 1
    even = 2

    1 -> 3 -> 2 -> 4 -> 5 -> 6 -> None
    odd = 3
    even = 4

    1 -> 3 -> 5 -> 2 -> 4 -> 6 -> None
    odd = 5
    even = 6

    1 -> 3 -> 5 -> 2 -> 4 -> 6 -> None

    -------------------------------------------------
    1 -> 2 -> 3 -> None
    odd = 1
    even = 2

    1 -> 3 -> 2 -> None
    odd = 3
    even = None
    """
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        odd = head
        even = head.next
        while even and even.next:
            tmp = odd.next
            odd.next = even.next
            even.next = even.next.next
            odd.next.next = tmp
            odd = odd.next
            even = even.next
        return head