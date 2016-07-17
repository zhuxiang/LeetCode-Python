class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        self.generator(result, "", n, 0)
        return result
        
    def generator(self, result, s, l, r):
        if l == 0 and r == 0:
            result.append(s)
            return
        if l > 0:
            self.generator(result, s + '(', l - 1, r + 1)
        if r > 0:
            self.generator(result, s + ')', l, r - 1)