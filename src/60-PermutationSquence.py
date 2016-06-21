class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        # create an array of factorial lookup
        factorial = []
        sum = 1
        factorial.append(1)
        for i in xrange(1,n):
            sum *= i
            factorial.append(sum)

        # create the array for permutation
        arrOrigin = []
        for i in xrange(1,n+1):
            arrOrigin.append(str(i))

        # element starts from array[0]
        k = k - 1
        arrResult = []
        # calculate the permutation sequence
        for i in xrange(n):
            index = k / factorial[n-1-i]
            arrResult.append(arrOrigin[index])
            arrOrigin.remove(arrOrigin[index])
            k = k % factorial[n-1-i]
        return ''.join(arrResult)

if __name__ == '__main__':
    s = Solution();
    sequence = s.getPermutation(4,14)
    print sequence
