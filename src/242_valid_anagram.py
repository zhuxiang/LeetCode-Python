class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s==None and t==None:
            return True
        elif s==None or t==None:
            return False
        elif len(s) != len(t):
            return False
        else:
            s = sorted(s)
            t = sorted(t)
            for (x,y) in zip(s,t):
                if x != y: return False
            return True

if __name__ == '__main__':
    s = "anagram"
    t = "nagaram"
    so = Solution()
    flag = so.isAnagram(s,t)
    print flag
