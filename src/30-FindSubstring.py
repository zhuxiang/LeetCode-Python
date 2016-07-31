class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """

    def generateSubstrings(this, words):
        """
        :type words: List[str]
        :rtype substrings: List[str]
        """
        if len(words) == 1:
            yield words[0]
        else:
            for substring in self.generateSubstrings(words[:-1]):
                

    def makeNext(this, pat):
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
        next = [0] * m
        while q < m:
            if k > 0 and pat[q] != pat[k]:
                k = next[k - 1]
            if pat[q] == pat[k]:
                k += 1
            next[q] = k
            q += 1
        return next
