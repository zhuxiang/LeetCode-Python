# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        headNew = ListNode(None)
        pre, pre.next = headNew, head
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            pre.next, b.next, a.next = b, a, b.next
            pre = a
        return headNew.next
    
if __name__ == '__main__':
    l1 = ListNode(1)
    l2 = ListNode(2)
    l1.next = l2
    head = l1
    s = Solution()
    headNew =  s.swapPairs(head)
    while headNew:
        print headNew.val
        headNew = headNew.next