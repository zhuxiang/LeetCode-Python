import sys

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        numsSorted = sorted(nums)
        minDiff, minS = sys.maxint, None
        i = 0
        while i < len(numsSorted) - 2:
            if i != 0 and numsSorted[i] == numsSorted[i-1]:
                i += 1
                continue
            n1 = numsSorted[i]
            j, k = i + 1, len(numsSorted) - 1
            while j < k:
                n2, n3 = numsSorted[j], numsSorted[k]
                s = n1 + n2 + n3
                d = abs(target - s)
                if d == 0:
                    return s
                if d < minDiff:
                    minS = s
                    minDiff = d
                if s < target:
                    j += 1
                    while numsSorted[j] == numsSorted[j-1] and j < k:
                        j += 1
                else:
                    k -= 1
                    while numsSorted[k] == numsSorted[k+1] and j < k:
                        k -= 1
            i += 1
        return minS

if __name__ == '__main__':
    nums = [-1, 2, 1, -4]
    s = Solution()
    print s.threeSumClosest(nums, 1)
