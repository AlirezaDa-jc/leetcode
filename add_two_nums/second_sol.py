# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        extra = 0
        head = None
        curr = None
        while l1 is not None or l2 is not None:
            sum = 0
            if l1 is not None:
                sum += l1.val
                l1 = l1.next
            if l2 is not None:
                sum += l2.val
                l2 = l2.next
            sum += extra
            node = ListNode(sum % 10)
            if head is None:
                head = node
            else:
                curr.next = node
            curr = node
            extra = sum // 10
        if extra != 0:
            node = ListNode(extra)
            curr.next = node
        return head
