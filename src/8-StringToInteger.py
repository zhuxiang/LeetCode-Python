class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        strStrip = list(str.strip())
        n = len(strStrip)
        if n == 0:
            return 0
        symbol = -1 if strStrip[0]=='-' else 1
        if strStrip[0] in ['-','+']: del strStrip[0]
        nDelSymbol = len(strStrip)
        sumStr = 0
        for i in xrange(nDelSymbol):
            if strStrip[i].isdigit():
                sumStr = sumStr*10 + ord(strStrip[i]) - ord('0')
            else:
                break
        return max(-2**31, min(2**31-1, symbol*sumStr))


if __name__ == '__main__':
    s = Solution();
    str = "2147483648"
    print s.myAtoi(str)
    print 2**31
