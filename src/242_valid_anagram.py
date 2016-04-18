class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        flag = False
        s_dic = self.turn2dic(s)
        t_dic = self.turn2dic(t)
        # print s_dic
        # print t_dic
        if len(s_dic)==len(t_dic):
            dic_equal = True
            for key in s_dic.keys():
                if not t_dic.has_key(key):
                    dic_equal = False
                    break
                elif s_dic[key] != t_dic[key]:
                    dic_equal = False
                    break
            flag = dic_equal
        return flag

    def turn2dic(self, s):
        s_dic = {}
        for char in s:
            if s_dic.has_key(char):
                s_dic[char] += 1
            else:
                s_dic[char] = 1
        return s_dic

if __name__ == '__main__':
    s = "anagram"
    t = "nagaram"
    so = Solution()
    flag = so.isAnagram(s,t)
    print flag
