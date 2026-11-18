# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None: return ListNode().next
        i =0
        temp = head
        while temp:
            i+=1
            temp = temp.next

        n = i-n
        if n==0:
            return head.next

        temp =  head
        for _ in range(n-1):
            temp = temp.next

        next = None
        if temp.next:
            next = temp.next.next
        temp.next = next
        
        return head