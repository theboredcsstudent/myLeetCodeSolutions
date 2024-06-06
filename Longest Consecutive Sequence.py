"""
Problem:
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [100,4,200,1,3,2]

Output: 4

Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]

Output: 9
 

Constraints:

0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
"""

class Solution(object):
    def longestConsecutive(self, nums):
        # First, we need to verify if the input has no empty values.
        if not nums:
            return 0
            """ this is optional since I already know that there will not 
            be an empty input but nevertheless... """
        
        # Next, we need to have a list that converts into a set which makes the process of looking up a value efficient.
        num_set = set(nums)
        # Next, we need to have a variable that keeps track of the longest streak found.
        longest_streak = 0

        # Next, we need to loop through each number in the set. We also want to check if the current number is the start of the set by analyzing if it is the smallest input there is.
        for num in num_set:
            if num - 1 not in num_set:
                # If it’s the start, we then place the current number to the num variable and set the current streak to 1. 
                current_num = num
                current_streak = 1

                """
                Then we use a while loop to count the length of the sequence by checking consecutive numbers. 
                Then as it goes on, we update the current_num and current_streak.
                """
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1
                
                # After exiting the while loop, we then update the longest_streak if the current sequence is longer than the previously recorded sequences.
                longest_streak = max(longest_streak, current_streak)
        
        # Lastlym we return the value of the longest_streak.
        return longest_streak