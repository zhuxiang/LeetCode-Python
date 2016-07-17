from Queue import PriorityQueue
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKListsInferior(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        k = len(lists)
        head = headCursor = None
        flag = False
        
        firstVal = float('inf')
        firstValIndex = -1
        for i in xrange(k):
            if lists[i]:
                flag = True
                if lists[i].val < firstVal:
                    firstVal = lists[i].val
                    firstValIndex = i
        if firstValIndex != -1:
            head = headCursor = lists[firstValIndex]
            lists[firstValIndex] = lists[firstValIndex].next
        
        while flag:
            flag = False
            minValNow = float('inf')
            minValIndex = -1
            i = 0
            while i < len(lists):
                if lists[i] != None:
                    flag = True
                    if lists[i].val < minValNow:
                        minValNow = lists[i].val
                        minValIndex = i
                    i += 1
                else:
                    lists.remove(lists[i])
            if minValIndex != -1:
                headCursor.next = lists[minValIndex]
                headCursor = headCursor.next
                lists[minValIndex] = lists[minValIndex].next
        
        return head
    

    def mergeKLists(self, lists):
        dummy = ListNode(None)
        curr = dummy
        q = PriorityQueue()
        for node in lists:
            if node: q.put((node.val,node))
        while q.qsize()>0:
            curr.next = q.get()[1]
            curr=curr.next
            if curr.next: q.put((curr.next.val, curr.next))
        return dummy.next
                
if __name__ == '__main__':
    s = Solution()
    l1 = ListNode(4)
    l2 = ListNode(1)
    l3 = ListNode(3)
    lists = [l1,l2,l3]
    head = s.mergeKLists(lists)
    while head:
        print head.val
        head = head.next