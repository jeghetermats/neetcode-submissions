# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        l = []
        curr = head
        while curr:
            l.append(curr)
            curr = curr.next
        
        i = 0
        head2 = tail = ListNode()
        while i<len(l):
            if i %2==0:
                tail.next = head
                head = head.next
            else:
                tail.next = l[len(l)-1-i//2]

            i+=1
            tail = tail.next
        tail.next = None


        head = head2.next