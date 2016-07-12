class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(nums1), len(nums2)
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m
        if n == 0:
            return None
        iMin, iMax, half = 0, m, (m + n + 1) / 2
        while iMin <= iMax:
            i = (iMin + iMax) / 2
            j = half - i
            if j > 0 and i < m and nums2[j-1] > nums1[i]:
                iMin = i + 1
            elif i > 0 and j < n and nums1[i-1] > nums2[j]:
                iMax = i - 1
            else:
                if i == 0:
                    maxOfLeft = nums2[j-1]
                elif j == 0:
                    maxOfLeft = nums1[i-1]
                else:
                    maxOfLeft = max(nums1[i-1], nums2[j-1])

                if (m + n) % 2 == 1:
                    return maxOfLeft

                if i == m:
                    minOfRight = nums2[j]
                elif j == n:
                    minOfRight = nums1[i]
                else:
                    minOfRight = min(nums1[i], nums2[j])

                return (maxOfLeft + minOfRight) / 2.0
