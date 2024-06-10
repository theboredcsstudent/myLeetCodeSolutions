"""
Problem:
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index_1] and numbers[index_2] where 1 <= index_1 < index2_ <= numbers.length.

Return the indices of the two numbers, index_1 and index_2, added by one as an integer array [index_1, index_2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

 

Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index_1 = 1, index_2 = 2. We return [1, 2].
Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index_1 = 1, index_2 = 3. We return [1, 3].
Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index_1 = 1, index_2 = 2. We return [1, 2].
 

Constraints:

2 <= numbers.length <= 3 * 10^4
-1000 <= numbers[i] <= 1000
numbers is sorted in non-decreasing order.
-1000 <= target <= 1000
The tests are generated such that there is exactly one solution.
"""

class Solution(object):
    def twoSum(self, numbers, target):
        # First, we need to initialize the pointers, left and right. Left will be set to the start of the array while right to the end. 
        left, right = 0, len(numbers) - 1

        """
        Next, for our loop, we will compute the sum of the numbers at the left and right pointers. 
        If the sum matches the target, we return the index of those numbers. 
        If the sum is less than the target, it means that we need a larger sum, so we increment the left pointer to move to the next higher number. 
        If the sum is greater than the target, we need a smaller sum so we decrement the right pointer to move to the next lower number.
        """
        while left < right:
            current_sum = numbers[left] + numbers[right]

            if current_sum == target:
                return[left + 1, right + 1]
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        # Lastly, we continue this process until the correct sum is found. 