"""
Problem:

Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

Example 1:
Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.

Example 2: 
Input: heights = [2,4]
Output: 4

Constraints:

1 <= heights.length <= 105
0 <= heights[i] <= 104
"""

class Solution(object):
    def largestRectangleArea(self, heights):
        # First, we need to initialize the variables for our stacks which will store the maximum rectangle area and index for iteration over the heights array.
        stack = []
        max_area = 0
        index = 0

        """
        Next, for our loop, we will check if the stack is empty or the current bar is taller than the bar at the top of the stack. 
        We then push the index onto the stack and move to the next bar. 
        But if the current bar is shorter, we pop the top of the stack and calculate the area using the height of the popped bar. 
        The width is then determined by the difference between the current index and the new top of the stack.
        """
        while index < len(heights):
            if not stack or heights[index] >= heights[stack[-1]]:
                stack.append(index)
                index += 1
            else:
                top_of_stack = stack.pop()
                area = (heights[top_of_stack] * ((index - stack[-1] - 1) if stack else index))
                max_area = max(max_area, area)

        """
        Lastly, after iterating through all the bars, there might be some bars left in the stack, so we pop each bar and calculate the area in a similar manner as above. 
        Then of course, we return the maximum area we found.
        """
        while stack:
            top_of_stack = stack.pop()
            area = (heights[top_of_stack] * ((index - stack[-1] -1) if stack else index))
            max_area = max(max_area, area)
        
        return max_area
        