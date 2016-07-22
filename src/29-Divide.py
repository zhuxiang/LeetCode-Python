class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor == 0:
            return -1
        positive = (dividend < 0) == (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        tmp, i = divisor, 1
        res = 0
        while dividend >= (tmp << 1):
            tmp <<= 1
            i <<= 1
        while tmp >= divisor and dividend >= divisor:
            if dividend >= tmp:
                dividend -= tmp
                res += i
            tmp >>= 1
            i >>= 1
        if not positive: res = -res
        return min(max(res, -2**31), 2**31-1)

if __name__ == '__main__':
    s = Solution()
    dividend = 12
    divisor = 6
    print s.divide(dividend, divisor)