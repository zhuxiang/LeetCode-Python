class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n!=0:
            nums.sort()
            numsLeft = []
            numsRight = []
            middle = n/2
            if n%2:
                for i in xrange(middle):
                    numsLeft.append(nums[i])
                    numsRight.append(nums[middle+i+1])
                numsLeft.append(nums[middle])
            else:
                for i in xrange(middle):
                    numsLeft.append(nums[i])
                    numsRight.append(nums[middle+i])
            numsLeft.reverse()
            numsRight.reverse()
            for j in xrange(n):
                nums[j] = numsRight[j/2] if j%2 else numsLeft[j/2]

if __name__ == '__main__':
    s = Solution()
    nums = [1,5,1,1,6,4]
    s.wiggleSort(nums)
    print nums
