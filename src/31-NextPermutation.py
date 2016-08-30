class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # find the longest non-decreasing suffix in nums
        right = len(nums) - 1
        while right >= 1 and nums[right] <= nums[right - 1]:
        	right -= 1
        if right == 0:
        	return self.reverse(nums, 0, len(nums) - 1)

        # find pivot
        pivot = right - 1
        # find rightmost succesor
        for i in xrange(len(nums) - 1, pivot, -1):
        	if nums[i] > nums[pivot]:
        		succesor = i
        		break
        # swap pivot and succesor
        nums[pivot], nums[succesor] = nums[succesor], nums[pivot]
        # reverse the suffix
        self.reverse(nums, pivot + 1, len(nums) - 1)

    def reverse(self, nums, l, r):
    	"""
    	reverse nums[l:r]
    	:type nums: List[int]
    	:type l: int
    	:type r: int
    	:rtype None
    	"""
    	while l < r:
    		nums[l], nums[r] = nums[r], nums[l]
    		l += 1
    		r -= 1