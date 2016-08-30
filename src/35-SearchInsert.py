class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        middle = 0
        while left < right:
        	middle = left + (right - left) / 2
        	if nums[middle] == target:
        		break
        	elif nums[middle] > target:
        		right = middle - 1
        	else:
        		left = middle + 1
       	if nums[left] == target:
       		middle = left
       	elif nums[middle] != target:
       		if nums[left] > target:
       			middle = left
       		else:
       			middle = left + 1
       	return middle

if __name__ == '__main__':
	sol = Solution()
	nums = [1]
	target = 0
	print sol.searchInsert(nums, target)