class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        # get the number of the gas stations
        n = len(gas)
        # try every gas station
        for i in xrange(n):
            gasInTank = 0
            count = 0
            j = i
            while gasInTank >= 0 and gas[j%n] + gasInTank >= cost[j%n] and count < n:
                gasInTank += gas[j%n] - cost[j%n]
                j += 1
                count += 1
            if count == n:
                return i
        return -1
