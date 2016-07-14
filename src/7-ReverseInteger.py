class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x > 2**31 or x < -2**31:
            return 0
        s = str(x)
        xReverse = 0
        if s[0] == '-':
            xReverse = -int(s[1:len(s)][::-1])
        else:
            xReverse = int(s[::-1])
        if xReverse > 2**31 or xReverse < -2**31:
            return 0
        else:
            return xReverse
