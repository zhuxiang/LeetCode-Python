class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maximumArea = area = 0
        leftIndex, rightIndex = 0, len(height) - 1
        while leftIndex < rightIndex:
            l, r = height[leftIndex], height[rightIndex]
            if l < r:
                area = (rightIndex - leftIndex) * l
                while l >= height[leftIndex]:
                    leftIndex += 1
            else:
                area = (rightIndex - leftIndex) * r
                while r >= height[rightIndex] and rightIndex:
                    rightIndex -= 1
            maximumArea = max(maximumArea, area)
        return maximumArea
