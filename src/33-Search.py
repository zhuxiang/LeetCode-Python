class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i = 0
        if nums[i] == target:
        	return i
        elif nums[i] < target:
        	while nums[i] < target and i < len(nums) - 1:
        		i += 1
        	if nums[i] == target:
        		return i
        	else:
        		return -1
        elif nums[i] > target:
        	while nums[i] > target and i > -len(nums):
        		i -= 1
        	if nums[i] == target:
        		return len(nums) + i
        	else:
        		return -1