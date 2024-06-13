"""
Problem:
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

Example 1:

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-10^4 <= matrix[i][j], target <= 10^4
"""

class Solution(object):
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False
        
        # First, we need to initialize the variables for our binary search, which will store the dimensions of the matrix and the pointers for the left and right indices of our conceptual 1D array.
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1

        # Next, for our binary search loop, we will calculate the midpoint index and convert it back to 2D indices to get the value at the position in the matrix.
        while left <= right:
            mid = (left + right) // 2
            mid_value = matrix[mid // n][mid % n]

            # We then compare this value with the target. If they are equal, we return True. 
            if mid_value == target:
                return True
            # If the current value is less than the target, we move the left pointer to mid + 1. Otherwise, we move the right pointer to mid - 1.
            elif mid_value < target:
                left = mid + 1
            else:
                right = mid - 1
        # Finally, if the loop completes without finding the target, we return False. This ensures we efficiently search the matrix in logarithmic time, leveraging its sorted properties.
        return False