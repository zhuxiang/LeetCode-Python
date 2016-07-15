# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        index = []
        p = head
        while p:
            index.insert(0, p)
            p = p.next
        if n == len(index):
            return head.next
        elif n == 1:
            index[1].next = None
            return head
        else:
            index[n].next = index[n-2]
            return head