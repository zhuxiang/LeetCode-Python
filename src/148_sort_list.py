# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        val = head.val
        # print val
        head_small = ListNode(None)
        head_large = ListNode(None)
        head_equal = ListNode(None)
        pivot_small = head_small
        pivot_large = head_large
        pivot_equal = head_equal
        pivot = head
        while pivot:
            if pivot.val < val:
                pivot_small.next = pivot
                pivot_small = pivot_small.next
            elif pivot.val > val:
                pivot_large.next = pivot
                pivot_large = pivot_large.next
            else:
                pivot_equal.next = pivot
                pivot_equal = pivot_equal.next
            list_node = pivot.next
            pivot.next = None
            pivot = list_node



        sorted_head_small = self.sortList(head_small.next)
        sorted_head_large = self.sortList(head_large.next)
        # merge the list


        if not sorted_head_small:
            pivot_equal.next = sorted_head_large
            return head_equal.next
        else:
            tail_small = sorted_head_small
            while tail_small.next:
                tail_small = tail_small.next
            tail_small.next = head_equal.next
            pivot_equal.next = sorted_head_large
            return sorted_head_small

if __name__ == '__main__':
    l1 = ListNode(3)
    l2 = ListNode(1)
    l3 = ListNode(4)
    l4 = ListNode(2)
    l5 = ListNode(5)
    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5
    s = Solution()
    l = s.sortList(l1)
    while l:
        print l.val
        l = l.next
