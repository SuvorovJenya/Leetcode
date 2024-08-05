# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return abs(a)

        curr, curr_next = head, head.next

        while curr_next:
            node = ListNode(gcd(curr.val, curr_next.val), curr_next)
            curr.next = node
            curr = curr_next
            curr_next = curr.next
            
        return head