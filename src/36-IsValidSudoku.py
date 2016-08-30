class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        mapRow = [{} for i in xrange(9)]
        mapCol = [{} for i in xrange(9)]
        mapCell = [[{} for i in xrange(3)] for j in xrange(3)]
        for i in xrange(9):
            for j in xrange(9):
                char = board[i][j]
                if char == '.':
                    continue
                if char in mapRow[i]:
                    return False
                else:
                    mapRow[i][char] = [i,j]
                if char in mapCol[j]:
                    return False
                else:
                    mapCol[j][char] = [i,j]
                if char in mapCell[i/3][j/3]:
                    return False
                else:
                    mapCell[i/3][j/3][char] = [i,j]
        return True

if __name__ == '__main__':
    sol = Solution()
    board = ["..4...63.",
             ".........",
             "5......9.",
             "...56....",
             "4.3.....1",
             "...7.....",
             "...5.....",
             ".........",
             "........."]
    print sol.isValidSudoku(board)