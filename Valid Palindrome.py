"""
Problem:
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 

Constraints:

1 <= s.length <= 2 * 10^5
s consists only of printable ASCII characters.
"""

class Solution(object):
    def isPalindrome(self, s):
        # First, we convert the entire string to lowercase so that the comparison will not be case-insensitive.
        s = s.lower()
        
        """ 
        Next, we will remove non-alphanumeric characters. 
        If it doesn’t have any numbers or symbols, we will then check if it is a palindrome. 
        We just need to reverse the string and check if it’s the same.
        """
        cleaned = ''.join(char for char in s if char.isalnum())

        return cleaned == cleaned[::-1]