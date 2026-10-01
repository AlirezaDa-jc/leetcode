# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        arr1 = []
        arr2 = []
        while l1 is not None or l2 is not None:
            if l1 is not None:
                arr1.append(l1.val)
                l1 = l1.next
            if l2 is not None:
                arr2.append(l2.val)
                l2 = l2.next
        arr1.reverse()
        arr2.reverse()
        num1 = int("".join(map(str, arr1)))
        num2 = int("".join(map(str, arr2)))
        num = num1 + num2
        num_arr = [int(d) for d in str(num)]
        print(num_arr)
        num_arr.reverse()
        head = ListNode(num_arr[0])
        curr = head
        for val in num_arr[1:]:
            curr.next = ListNode(val)
            curr = curr.next
        return head
