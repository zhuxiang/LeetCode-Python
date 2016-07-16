class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for c in s:
            if c in ['(', '{', '[']:
                stack.append(c)
                continue
            elif c == ')':
                if len(stack) > 0 and stack[-1] == '(':
                    stack.pop()
                else:
                    return False
                continue
            elif c == '}':
                if len(stack) > 0 and stack[-1] == '{':
                    stack.pop()
                else:
                    return False
                continue
            elif c == ']':
                if len(stack) > 0 and stack[-1] == '[':
                    stack.pop()
                else:
                    return False
                continue
            else:
                return False
            
        return stack == []

if __name__ == '__main__':
    s = "[]"
    v = Solution()
    print v.isValid(s)