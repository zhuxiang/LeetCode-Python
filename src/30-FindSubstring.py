class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        resPos = set()
        wordCnt = len(words)
        if wordCnt == 0:
            return resPos
        wordLen = len(words[0])
        substrings = set(self.generateSubstrings(words, wordLen))
        n = len(s)
        for substring in substrings:
            m = len(substring)
            i, q = 0, 0
            nextDict = self.makeNext(substring)
            while i < n:
                while q > 0 and substring[q] != s[i]:
                    q = nextDict[q - 1]
                if substring[q] == s[i]:
                    q += 1
                if q == m:
                    resPos.add(i - m + 1)
                    q = nextDict[q - 1]
                i += 1
        return list(resPos)

    def generateSubstrings(self, words, wordLen):
        """
        :type words: List[str]
        :type wordLen: int
        :rtype substrings: List[str]
        """
        if len(words) == 1:
            yield words[0]
        else:
            for substring in self.generateSubstrings(words[:-1], wordLen):
                for i in xrange(len(words)):
                    yield substring[:i*wordLen] + words[-1] + substring[i*wordLen:]

    def makeNext(self, pat):
        """
        :type pat: str
        :rtype next: List[int]
        """
        # q: the index of pat
        # k: the length of maximum prefix and suffix
        q, k = 1, 0
        # m: the length of pat
        m = len(pat)
        # next: partial match dict for KMP algorithm
        nextDict = [0] * m
        while q < m:
            while k > 0 and pat[q] != pat[k]:
                k = nextDict[k - 1]
            if pat[q] == pat[k]:
                k += 1
            nextDict[q] = k
            q += 1
        return nextDict

if __name__ == '__main__':
    s = str("aaa")
    words = ["a","a"]
    sol = Solution()
    print sol.findSubstring(s, words)
