""" 
Problem:
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 

Constraints:

3 <= nums.length <= 3000
-10^5 <= nums[i] <= 10^5
"""

class Solution(object):
    def threeSum(self, nums):
        # First, we need to sort the input and initialize an empty list.
        nums.sort()
        result = []

        # Next, we loop through the sorted array. For each element, we check if it is a duplicate of the previous element to avoid redundant triplets.
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            """
            Next, we then initialize two pointers, one starting just after the current element and the other at the end of the array. 
            Using these pointers, we can check if the sum of the element equals to zero. If the sum is less than zero, we increment the left pointer to increase the sum. 
            If the sum is greater than zero, we decrement the right pointer to decrease the sum. 
            If the sum is zero, we add the triplet to our results list. We also skip any duplicates to ensure all triplets are unique.
            """
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        # Lastly, after completing the loop, we return the list of unique triplets that sum up to zero.
        return result