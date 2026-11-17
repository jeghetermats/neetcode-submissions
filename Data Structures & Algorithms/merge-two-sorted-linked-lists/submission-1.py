# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2: return ListNode().next
        curr1, curr2 = list1,list2
        head = tail = ListNode()

        while curr1 or curr2:
            if curr1 and curr2:
                tail.next = curr1 if curr1.val < curr2.val else curr2
            else: tail.next = curr1 or curr2
            


            if tail.next == curr1:
                curr1 = curr1.next
            else:
                curr2 = curr2.next
            tail = tail.next

        return head.next