"""
Problem:
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example 1:

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:

Input: height = [1,1]
Output: 1
 

Constraints:

n == height.length
2 <= n <= 10^5
0 <= height[i] <= 10^4
"""

class Solution(object):
    def maxArea(self, height):
        """
        First, we need to initialize the variables for the two pointers. 
        We set the left pointer at the start and the right pointer at the end.
        """
        left, right = 0, len(height) - 1
        max_area = 0

        """
        Next, we do a loop that will check if the left pointer is less than the right pointer. Inside the loop, we will then calculate the width between the two pointers and determine the current height as the minimum of the heights at the left and right pointers. 
        We will then compute the area by multiplying the width by the current height and update the max_area if the computed area is greater.
        If the height at the left pointer is less than the right pointer, we move it one step to the right to potentially find a taller bar. 
        Otherwise, we move the right pointer one step to the left.
        """
        while left < right:
            width = right - left
            current_height = min(height[left], height[right])
            current_area = width * current_height

            max_area = max(max_area, current_area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        # Lastly, we store our maximum area in the max_area variable then return this as the result.
        return max_area