"""
Problem:
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

 

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]
 

Constraints:

1 <= temperatures.length <= 10^5
30 <= temperatures[i] <= 100
"""

class Solution(object):
    def dailyTemperatures(self, temperatures):
        # First, we need to initialize variables for the temperatures, answer, and stack.
        n = len(temperatures)
        answer = [0] * n
        stack = [0]

        """ Next, we then loop through each day’s temperature. 
        We use enumerate(temperatures) to get both the index and the temperature for each day.
        If true, we will pop the index from the stack, and calculate the difference in days between the current day and the popped day, and store the difference in the answer variable.
        """
        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                idx = stack.pop()
                answer[idx] = i -idx
            # After the while loop, we then push the current day’s index onto the stack. 
            stack.append(i)

        # Finally, we return the answer.
        return answer