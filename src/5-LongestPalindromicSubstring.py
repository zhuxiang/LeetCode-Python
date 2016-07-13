class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        lenS = len(s)
        if lenS == 0:
            return None
        maxLen = 1
        start = 0
        for i in xrange(lenS):
            if i - maxLen >= 1 and s[i-maxLen-1:i+1] == s[i-maxLen-1:i+1][::-1]:
                start = i - maxLen - 1
                maxLen += 2
                continue
            if i - maxLen >= 0 and s[i-maxLen:i+1] == s[i-maxLen:i+1][::-1]:
                start = i - maxLen
                maxLen += 1
        return s[start:start+maxLen]
