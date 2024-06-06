"""
Problem:
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 10^4
-10^9 <= nums[i] <= 10^9
-10^9 <= target <= 10^9
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n^2) time complexity?
"""

class Solution(object):
    def twoSum(self, nums, target):
        # First, we need to initialize a dictionary to store the inputs. This will give us the efficiency we need to achieve less than O(n^2) time complexity.
        num_to_index = {}

        for index, num in enumerate(nums):
            """
            Next, we need to compute the “complement” of the target number. 
            The logic here is, for example our target is 9, and our input is [2,7,11,15], 
            then we will first minus 9 to 2 which will yield us 7, and whatever the result is, 
            we will check our index if there is a 7, then the code will return us the index of both the one that we minus and the result.
            But, if we don’t find the complement in the dictionary, we store the current number in the dictionary as well as its index. 
            This way, we will be able to keep track of every number that we encounter.
            """
            complement = target - num

            if complement in num_to_index:
                return [num_to_index[complement], index]

            num_to_index[num] = index