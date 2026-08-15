# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        newHead = ListNode(head.val)
        head = head.next

        while head:
            if head.val <= newHead.val:
                newHead = ListNode(head.val, next=newHead)
            else:
                curr = newHead
                while curr:
                    if curr.next:
                        if curr.next.val >= head.val:
                            temp = curr.next
                            curr.next = ListNode(head.val)
                            curr.next.next = temp
                            break
                    else:
                        curr.next = ListNode(head.val)
                        break
                    curr = curr.next

            head = head.next

        return newHead