# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = list1
        curr2 = list2
        if not list1 or not list2:
            return list1 or list2
        elif curr1.val <= curr2.val:
            headx = curr1
            curr1 = curr1.next
        elif curr1.val > curr2.val:
            headx = curr2
            curr2 = curr2.next
        currx = headx
        while currx is not None:
            if curr1 is None and curr2 is None:
                currx.next = None
            elif curr1 is not None and curr2 is None:
                currx.next = curr1
                curr1 = curr1.next
            elif curr2 is not None and curr1 is None:
                currx.next = curr2
                curr2 = curr2.next
            elif curr1.val <= curr2.val:
                currx.next = curr1
                curr1 = curr1.next
            else:
                currx.next = curr2
                curr2 = curr2.next
            currx = currx.next
        return headx
                