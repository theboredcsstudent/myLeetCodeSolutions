"""
Problem:
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example 1:

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
 

Constraints:

n == height.length
1 <= n <= 2 * 10^4
0 <= height[i] <= 10^5
"""

class Solution(object):
    def trap(self, height):
        if not height:
            return 0

        """
        So, as any other pointer problem, we need to initialize the left and right pointers. 
        Then we should keep track of the maximum heights encountered from left to right.
        """
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        water_trapped = 0

        """
        Next, we then start a loop where we will analyze the elevation map from both ends towards the center. 
        If the height at the left pointer is less than or equal to the height of the right pointer, we update the variable left_max with maximum height and the current height at left.
        Next, we calculate the trapped water at that position by subtracting the current height and add that value to the water_trapped variable.
        Finally, we increment the left pointer to move to the next position.
        We then do the same with the right pointer but in reverse.
        """
        while left < right:
            if height[left] <= height[right]:
                left_max = max(left_max, height[left])
                water_trapped += left_max - height[left]
                left += 1
            else:
                right_max = max(right_max, height[right])
                water_trapped += right_max - height[right]
                right -= 1
        """
        Lastly, we continue this process until the left and right pointers meet. 
        Once the loop completes, we return the total amount of trapped water stored in the water_trapped variable.
        """
        return water_trapped