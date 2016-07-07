class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        total = 0
        start = 0
        n = len(gas)
        subsum = float('inf')
        for i in xrange(n):
            total += gas[i] - cost[i]
            if total < subsum:
                subsum = total
                start = i + 1
        return -1 if total < 0 else (start % n)
