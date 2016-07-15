class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == None or len(strs) == 0:
            return ""
        else:
            prefix = strs[0]
        for i in xrange(1,len(strs)):
            length = min(len(prefix), len(strs[i]))
            print length
            while prefix[0:length] != strs[i][0:length] and length > 0:
                length -= 1
            prefix = prefix[:length]
        return prefix

if __name__ == '__main__':
    s = Solution()
    strs = ["aaa", "aa", "aaa"]
    print s.longestCommonPrefix(strs)
