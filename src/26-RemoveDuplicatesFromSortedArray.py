class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        newTail = 0
        for i in xrange(1,len(nums)):
            if nums[i] != nums[newTail]:
                newTail += 1
                nums[newTail] = nums[i]
        return newTail + 1

if __name__ == '__main__':
    nums = [1,1,1,4,5]
    s = Solution()
    print s.removeDuplicates(nums)
    print nums