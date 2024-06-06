"""
Problem:
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
 

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""

# First, we need to import the Counter class as this will help us with efficiency in our code.
# The counter class will help us count the frequency of each element in the input array.
from collections import Counter

class Solution(object):
    def topKFrequent(self, nums, k):
        counter = Counter(nums)
        # Next, we use the most_common method of the counter class to get the k most frequent elements.
        # Lastly, we get the elements from the resulting list of tuples.
        return [num for num, _ in counter.most_common(k)]