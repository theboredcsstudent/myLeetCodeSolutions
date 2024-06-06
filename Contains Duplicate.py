"""
Problem:
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
 

Constraints:

1 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
"""

class Solution(object):
    def containsDuplicate(self, nums):
        # First, we need to declare an empty set which will house the elements.
        seen = set()
        # Next, using a for loop, the code will run through the input and store them in the set.
        for num in nums:
            # If the set already contains the duplicate then the code will return True, otherwise it will return False.
            if num in seen:
                return True
            seen.add(num)
        return False