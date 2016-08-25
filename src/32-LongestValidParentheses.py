class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        # index of "("
        stk = []
        # maximum length of valid parentheses
        maxLen = 0
        # the leftmost index
        left = -1
        for i in xrange(len(s)):
            if s[i] == '(':
                stk.append(i)
            else:
                if not stk:
                    left = i
                else:
                    stk.pop()
                    if not stk:
                        maxLen = max(maxLen, i - left)
                    else:
                        maxLen = max(maxLen, i - stk[-1])
        return maxLen
    
if __name__ == '__main__':
    Sol = Solution()
    s = "(()"
    print Sol.longestValidParentheses(s)