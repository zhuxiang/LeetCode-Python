class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # search the target number by binary search
        left, right = 0, len(nums) - 1
        index = 0
        flag = 0
        while left < right:
        	index = (right - left) / 2 + left
        	if nums[index] == target:
        		flag = 1
        		break
        	elif nums[index] > target:
        		right = index - 1
        	else:
        		left = index + 1
        if nums[left] == target:
        	index = left
        	flag = 1
        if not flag:
        	return [-1, -1]
        else:
        	leftRange = rightRange = index
        	while leftRange > 0 and nums[leftRange - 1] == nums[index]:
        		leftRange -= 1
        	while rightRange < len(nums) - 1 and nums[rightRange + 1] == nums[index]:
        		rightRange += 1
        	return [leftRange, rightRange]

if __name__ == '__main__':
	sol = Solution()
	nums = [1]
	target = 1
	print sol.searchRange(nums, target)