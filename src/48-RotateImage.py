class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        """
        * clockwise rotate
        * first reverse up to down, then swap the symmetry
        * 1 2 3     7 8 9     7 4 1
        * 4 5 6  => 4 5 6  => 8 5 2
        * 7 8 9     1 2 3     9 6 3
        """
        matrix.reverse()
        n = len(matrix)
        for i in xrange(n):
            for j in xrange(i+1,n):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]

if __name__ == '__main__':
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    s = Solution()
    s.rotate(matrix)
    print matrix
