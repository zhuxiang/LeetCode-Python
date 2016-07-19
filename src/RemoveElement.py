class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        begin = 0
        i = 0
        while i < len(nums):
            if nums[i] != val:
                nums[begin] = nums[i]
                begin += 1
            i += 1
        return begin