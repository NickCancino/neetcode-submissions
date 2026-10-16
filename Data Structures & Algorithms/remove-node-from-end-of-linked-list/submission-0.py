# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        arr = []
        while curr:
            arr.append(curr.val)
            curr = curr.next
        arr.pop(len(arr) - n)
        dummy = ListNode()
        curr = dummy
        for n in arr:
            curr.next = ListNode(n)
            curr = curr.next
        return dummy.next