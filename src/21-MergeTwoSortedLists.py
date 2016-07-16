# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 and not l2:
            return None
        elif not l1:
            return l2
        elif not l2:
            return l1
        else:
            head = l1 if l1.val < l2.val else l2
            headCursor, l1Cursor, l2Cursor = head, l1, l2
            if l1.val < l2.val:
                l1Cursor = l1Cursor.next
            else:
                l2Cursor = l2Cursor.next
            
            while l1Cursor and l2Cursor:
                if l1Cursor.val < l2Cursor.val:
                    headCursor.next = l1Cursor
                    l1Cursor = l1Cursor.next
                    headCursor = headCursor.next
                else:
                    headCursor.next = l2Cursor
                    l2Cursor = l2Cursor.next
                    headCursor = headCursor.next
            if l1Cursor:
                headCursor.next = l1Cursor
            if l2Cursor:
                headCursor.next = l2Cursor
            return head