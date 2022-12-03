# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # Using a simple recursion with the next function, to define the next node on the linked list
    def next(self, dec: int, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # recursion ending conditios (if there is no other node on l1 and l2 to iterate)
        if l1 is None and l2 is None:
             # if last node sum as bigger than 10, a final node with the decimal must be added, otherwise, no new node is needed
            if dec == 0:
                return None
            else:
                return ListNode(1)
        
        # If there was only one linked list still available, then its number will be the sole one to add, and prevents to try to call the .next attribute on a None object
        if l2 is None:
            # add with the decimal from last sum
            ans = l1.val + dec

            #  check if smaller than 10, if it's not, signal to next node add 1 to the sum
            if ans < 10:
                return ListNode(ans, next=self.next(0, l1.next, l2))
            return ListNode(ans%10, next=self.next(1, l1.next, l2)) # ans%10 -> to remove the decimal
        if l1 is None:
            ans = l2.val + dec
            if ans < 10:
                return ListNode(ans, next=self.next(0, l1, l2.next))
            return ListNode(ans%10, next=self.next(1, l1, l2.next))
 
        # Same logic as with only one node
        ans = l1.val + l2.val + dec
        
        if ans < 10:
            return ListNode(val=ans, next=self.next(0, l1.next, l2.next))
        else:
            return ListNode(val=ans%10, next=self.next(1, l1.next, l2.next))

        
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Initial sum, and call of the recursion
        ans = l1.val + l2.val        
        if ans < 10:
            return ListNode(val=ans, next=self.next(0, l1.next, l2.next))
        else:
            return ListNode(val=ans%10, next=self.next(1, l1.next, l2.next))