class Solution(object):
    def threeSumDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        numDict = {}
        for i in xrange(len(nums)):
            if numDict.has_key(nums[i]):
                numDict[nums[i]].append(i)
            else:
                numDict[nums[i]] = [i]
        # print numDict
        result = []
        for j in xrange(len(nums)):
            for k in xrange(j+1, len(nums)):
                complement = 0 - nums[j] - nums[k]
                if numDict.has_key(complement):
                    if len(numDict[complement]) == 1:
                        if numDict[complement][0] != j and numDict[complement][0] != k:
                            result.append([nums[j], nums[k], complement])
                    elif len(numDict[complement]) == 2:
                        if not (nums[i] == 0 and nums[j] == 0):
                            result.append([nums[j], nums[k], complement])
                    else:
                        result.append([nums[j], nums[k], complement])
        return result

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        numsSorted = sorted(nums)
        result = []
        for i in xrange(len(numsSorted) - 2):
            if i != 0 and numsSorted[i] == numsSorted[i-1]:
                continue
            j, k = i+1, len(numsSorted) - 1
            while j < k:
                s = numsSorted[i] + numsSorted[j] + numsSorted[k]
                if s == 0:
                    result.append([numsSorted[i], numsSorted[j], numsSorted[k]])
                    j += 1
                    k -= 1
                    while numsSorted[j] == numsSorted[j-1] and j < k:
                        j += 1
                    while numsSorted[k] == numsSorted[k+1] and j < k:
                        k -= 1
                elif s < 0:
                    j += 1
                    while numsSorted[j] == numsSorted[j-1] and j < k:
                        j += 1
                else:
                    k -= 1
                    while numsSorted[k] == numsSorted[k+1] and j < k:
                        k -= 1
        return result

if __name__ == '__main__':
    nums = [-2, 0, 1, 1, 2]
    s = Solution()
    print s.threeSum(nums)
