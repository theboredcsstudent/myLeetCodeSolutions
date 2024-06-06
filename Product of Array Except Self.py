"""
Problem:
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 10^5
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
"""

class Solution(object):
    def productExceptSelf(self, nums):
        # First, we need to create an array that is the same length as nums as this will store the result.
        n = len(nums)
        answer = [1] * n

        # Next, we need to go through the left products. We need to compute the product of all elements to the left and store it in the answer array.
        left_product = 1
        for i in range(n):
            # For each element nums[i}, we set answer[i] to left_product
            answer[i] = left_product
            left_product *= nums[i]

        # We do the same for the right products until we finish it.
        right_product = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= right_product
            right_product *= nums[i]
        
        # Then, of course, we return the answer.
        return answer