# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 1
        node = head
        while node.next != None:
            count += 1
            node = node.next
        node = head
        for _ in range(1, count - n):
            node = node.next
        if count == n:
            head = head.next
        elif node.next and node.next.next:
            node.next = node.next.next
        else:
            node.next = None
        return head
