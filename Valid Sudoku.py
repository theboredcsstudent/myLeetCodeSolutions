"""
Problem:
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:
Example 1:


Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

Example 2:

Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.

Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.
"""

class Solution(object):
    def isValidSudoku(self, board):
        # First, we need to initialize variables rows, cols, and boxes. This will track numbers in each row, column, and 3x3 boxes.
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        # Next, we need to loop through each cell in the board. We will check the next row, column, and box if the cell does not contain a digit. 
        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num == '.':
                    continue
                
                """
                Next, for each number, we will check if it’s already present in the next row, column, or box. 
                If it is, we will then return False because there’s a duplicate, otherwise, we add the digit to the respective variable.
                """
                if num in rows[r]:
                    return False
                rows[r].add(num)
            
                if num in cols[c]:
                    return False
                cols[c].add(num)

                box_index = (r // 3) * 3 + (c // 3)

                if num in boxes[box_index]:
                    return False
                boxes[box_index].add(num)
                
        # Lastly, the code will return True if the loop completes its goal without finding any duplicates.
        return True