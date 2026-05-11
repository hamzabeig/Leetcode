# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
#         if not lists:
#             return None
#         n = len(lists)
#         if n < 2:
#             return lists[0]
        
        
        
#         def recursion(output, r):
#             if r>=n:
#                 return output
#             output = merge(output, lists[r])

#             return recursion(output, r+1)

        # return recursion(lists[0],1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        def merge(cl,cr):
            if not cl:
                return cr
            if not cr:
                return cl
            if cl.val < cr.val:
                cl.next = merge(cl.next,cr)
                return cl
            else:
                cr.next = merge(cl,cr.next)
                return cr
        
        
        while len(lists) > 1:
            merged_lists = []
            
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                merged_lists.append(merge(l1, l2))
            
            lists = merged_lists
        
        return lists[0]


        