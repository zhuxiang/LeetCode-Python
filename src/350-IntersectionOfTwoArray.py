class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        numItersection = []
        # print len(nums1)
        # print len(nums2)
        if len(nums1) <= len(nums2):
            for n in nums1:
                if n in nums2:
                    nums2.remove(n)
                    numItersection.append(n)
        else:
            for n in nums2:
                # print n
                if n in nums1:
                    nums1.remove(n)
                    numItersection.append(n)
        return numItersection

if __name__ == '__main__':
    nums1 = [1,2]
    nums2 = [2,1]
    s = Solution()
    print s.intersect(nums1,nums2)
