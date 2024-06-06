"""
Problem:
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 10^4
s and t consist of lowercase English letters.
 

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
"""

# First, we need to import counter class which will help us count the characters.
from collections import Counter

class Solution(object):
    def isAnagram(self, s, t):
        # Next, we will use Counter() to count the characters inside the s and t argument.
        # Lastly, we simply compare the two counter results. If they are the same, then it will return true and false if not.
        return Counter(s) == Counter(t)