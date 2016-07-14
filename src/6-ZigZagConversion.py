class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s
        zigZagArr = [''] * numRows
        index, step = 0, 1
        for x in s:
            zigZagArr[index] += x
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step
        return ''.join(zigZagArr)
