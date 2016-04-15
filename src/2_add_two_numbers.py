# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1==None and l2==None:
            return None
        elif l1!=None and l2==None:
            return l1
        elif l1==None and l2!=None:
            return l2
        else:
            l_plus = ListNode(0)
            val = l1.val + l2.val
            l_plus.val = val % 10
            if val>9:
                tmp = self.addTwoNumbers(l1.next, l2.next)
                l_plus.next = self.addTwoNumbers(tmp,ListNode(1))
            else:
                l_plus.next = self.addTwoNumbers(l1.next, l2.next)
        return l_plus

if __name__ == '__main__':
    l11 = ListNode(2)
    l12 = ListNode(4)
    l13 = ListNode(3)
    l21 = ListNode(5)
    l22 = ListNode(6)
    l23 = ListNode(4)
    l11.next = l12
    l12.next = l13
    l21.next = l22
    l22.next = l23
    s = Solution()
    l_plus = s.addTwoNumbers(l11,l21)
    while l_plus!=None:
        print l_plus.val
        l_plus = l_plus.next
