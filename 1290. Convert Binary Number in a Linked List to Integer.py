# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        tmp = ''
        curr = head
        while curr:
            tmp += str(curr.val)
            curr = curr.next
        return int(tmp, 2)

