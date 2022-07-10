class Solution:
    def NQueens(self, col, n, board: List[str], result: List[List[str]], leftRow: List[int], lowerDiag: List[int], upperDiag: List[int]):
        
        # base case
        if col == n:
            # creating a copy to add in final result
            # for each row converting list to str
            copy = ["".join(row) for row in board]
            result.append(copy)
            return
        
        for row in range(0, n):
            if leftRow[row]==0 and lowerDiag[row+col]==0 and upperDiag[n-1+col-row]==0:
                board[row][col] = 'Q'
                leftRow[row] = 1
                lowerDiag[row+col] = 1
                upperDiag[n-1+col-row] = 1
                
                self.NQueens(col+1, n, board, result, leftRow, lowerDiag, upperDiag)
                
                board[row][col] = '.'
                leftRow[row] = 0
                lowerDiag[row+col] = 0
                upperDiag[(n-1)+(col-row)] = 0

            
    
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        # we cannot use direct str here as it is immutable so we use list
        board = [["." for i in range(n)] for j in range(n)]
        leftRow = [0 for i in range(n)]
        lowerDiag = [0 for i in range(2*n-1)]
        upperDiag = [0 for i in range(2*n+1)]

        self.NQueens(0, n, board, result, leftRow, lowerDiag, upperDiag)
        return result

'''
TC: O(n^2) (row*col)
SC: O(n + n + n + n^2) (leftRow,lowerdiag,upperDiag,board)
aux SC: O(n) [Depth]
'''