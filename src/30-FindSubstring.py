class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        wordLen = self.calWordLen(words)
        wordDict = self.genWordDict(words)
        n = wordLen * len(words)
        indexList = []
        for i in xrange(wordLen):
            start = i
            chkDict = {}
            cnt = 0
            for j in xrange(i, len(s) - wordLen + 1, wordLen):
                word = s[j:j+wordLen]
                if word in wordDict:
                    if word in chkDict:
                        chkDict[word] += 1
                    else:
                        chkDict[word] = 1
                    cnt += 1
                    while chkDict[word] > wordDict[word]:
                        chkDict[s[start:start+wordLen]] -= 1
                        start += wordLen
                        cnt -= 1
                    if cnt == len(words):
                        indexList.append(start)
                else:
                    chkDict = {}
                    start = j + wordLen
                    cnt = 0
        return indexList

    def calWordLen(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        if len(words) == 0:
            return 0
        else:
            return len(words[0])

    def genWordDict(self, words):
        """
        :type words: List[str]
        :rtype: Dict[int]
        """
        wordDict = {}
        for word in words:
            if wordDict.has_key(word):
                wordDict[word] += 1
            else:
                wordDict[word] = 1
        return wordDict

if __name__ == '__main__':
    sln = Solution()
    s = "wordgoodgoodgoodbestword"
    words = ["word","good","best","good"]
    print sln.findSubstring(s, words)