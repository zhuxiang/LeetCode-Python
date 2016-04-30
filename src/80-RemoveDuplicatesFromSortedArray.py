class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 3:
            return n
        i = 1
        cntSame = 1
        while i < n:
            if nums[i] == nums[i-1]:
                cntSame += 1
                if cntSame > 2:
                    nums.remove(nums[i])
                    i -= 1
                    n -= 1
            else:
                cntSame = 1
            i += 1
        return n


if __name__ == '__main__':
    nums = [1,1,1,2,2,2,2,2,3,3]
    s = Solution()
    s.removeDuplicates(nums)
    print nums
