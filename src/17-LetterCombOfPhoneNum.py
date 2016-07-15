class Solution(object):
    def letterCombinationsInferior(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        phoneTable = {}
        phoneTable["0"] = " "
        phoneTable["1"] = "*"
        phoneTable["2"] = "abc"
        phoneTable["3"] = "def"
        phoneTable["4"] = "ghi"
        phoneTable["5"] = "jkl"
        phoneTable["6"] = "mno"
        phoneTable["7"] = "pqrs"
        phoneTable["8"] = "tuv"
        phoneTable["9"] = "wxyz"

        result = [""]
        if len(digits) == 0:
            return []
        for digit in digits:
            tmp = []
            for oldDigit in result:
                for c in phoneTable[digit]:
                    tmp.append(oldDigit + c)
            result = tmp
        return result

    # better solution
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        s = "0 ,1*,2abc,3def,4ghi,5jkl,6mno,7pqrs,8tuv,9wxyz"
        phoneTable = {digit[0]:digit[1:] for digit in s.split(',')}
        return list(self.letterComb(digits, phoneTable))

    def letterComb(self, digits, phoneTable):
        if not digits:
            yield ''
        else:
            for i in self.letterComb(digits[:-1], phoneTable):
                for j in phoneTable[digits[-1]]:
                    yield i + j

if __name__ == '__main__':
    digits = "23"
    s = Solution()
    print s.letterCombinations(digits)
