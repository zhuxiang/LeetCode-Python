class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        numsSorted = sorted(nums)
        result = []
        i = 0
        while i < len(numsSorted)-3:
            if i != 0 and numsSorted[i] == numsSorted[i-1]:
                i += 1
                continue
            n1 = numsSorted[i]
            resultRemain = self.threeSum(numsSorted[i+1:], target - n1)
            if resultRemain:
                for arr in resultRemain:
                    result.append([n1] + arr)
            i += 1
        return result
        
    def threeSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        numsSorted = sorted(nums)
        result = []
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
                if s == target:
                    result.append([n1, n2, n3])
                    j += 1
                    k -= 1
                    while numsSorted[j] == numsSorted[j-1] and j < k:
                        j += 1
                    while numsSorted[k] == numsSorted[k+1] and j < k:
                        k -= 1
                elif s < target:
                    j += 1
                    while numsSorted[j] == numsSorted[j-1] and j < k:
                        j += 1
                else:
                    k -= 1
                    while numsSorted[k] == numsSorted[k+1] and j < k:
                        k -= 1
            i += 1
        return result

if __name__ == '__main__':
    s = Solution()
    nums = [-1,0,1,2,-1,-4]
    print s.fourSum(nums, -1)