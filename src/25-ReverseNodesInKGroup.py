# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k == 1:
            return head
        cur = tail = head
        count = 0
        while cur and count < k:
            cur = cur.next
            count += 1
        if count == k:
            head = self.reverseListK(head, k)
        while cur:
            headNew = tailNew = cur
            count = 0
            while cur and count < k:
                cur = cur.next
                count += 1
            if count == k:
                tail.next = self.reverseListK(headNew, k)
                tail = tailNew
        return head
        
    # reverse the first k ListNodes
    def reverseListK(self, head, k):
        tail = head
        i = 1
        while tail and tail.next and i < k:
            tmp = head
            head = tail.next
            tail.next = head.next
            head.next = tmp
            i += 1
        return head

if __name__ == '__main__':
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)
    l5 = ListNode(5)
    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5
    s = Solution()
    k = 2
    head = s.reverseKGroup(l1, k)
    while head:
        print head.val
        head = head.next