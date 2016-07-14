class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        sumInt = 0
        for c in s:
            if c == 'M':
                sumInt += 1000
            elif c == 'D':
                sumInt += 500
            elif c == 'C':
                sumInt += 100
            elif c == 'L':
                sumInt += 50
            elif c == 'X':
                sumInt += 10
            elif c == 'V':
                sumInt += 5
            elif c == 'I':
                sumInt += 1

        if s.find('CD') != -1 or s.find('CM') != -1:
            sumInt -= 200
        if s.find('XL') != -1 or s.find('XC') != -1:
            sumInt -= 20
        if s.find('IV') != -1 or s.find('IX') != -1:
            sumInt -= 2

        return sumInt
