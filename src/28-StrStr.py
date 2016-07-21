class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n, m = len(haystack), len(needle)
        if m == 0:
            return 0
        elif n == 0:
            return -1
        i, q = 0, 0
        next = self.makeNext(needle)
        while i < n:
            while q > 0 and needle[q] != haystack[i]:
                q = next[q - 1]
            if needle[q] == haystack[i]:
                q += 1
            if q == m:
                return i - m + 1
            i += 1
        return -1
    
    # KMP algorithm
    def makeNext(self, pat):
        """
        :type pat: str
        :rtype int[]
        """
        # initialize
        # q: the index of pat
        # k: the length of maximum prefix and suffix pair
        q, k = 1, 0
        # m: length of pat
        m = len(pat)
        # next: partial match dict
        next = [0] * m
        while q < m:
            while k > 0 and pat[k] != pat[q]:
                k = next[k - 1]
            if pat[k] == pat[q]:
                k += 1
            next[q] = k
            q += 1
        return next

if __name__ == '__main__':
    needle = "abcabcacab" 
    haystack = ""
    s = Solution()
    print s.makeNext(needle)
    print s.strStr(haystack, needle)