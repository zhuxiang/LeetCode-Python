class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        n = len(nums)
        for i in xrange(n):
            dic[nums[i]]=i
        print dic
        for i in xrange(n):
            complement = target - nums[i]
            if dic.has_key(complement) and dic[complement]!=i:
                return [i,dic[complement]]

if __name__ == '__main__':
    solution = Solution()
    nums = [1,2,2]
    target = 4
    print solution.twoSum(nums,target)
