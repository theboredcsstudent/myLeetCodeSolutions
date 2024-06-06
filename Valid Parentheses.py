"""
Problem:
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 10^4
s consists of parentheses only '()[]{}'.
"""

class Solution(object):
    def isValid(self, s):
        # First, we need a dictionary that stores the pairs of closing and opening brackets.
        matching_bracket = {')' : '(', '}' : '{', ']' : '['}
        # Next, we then use a stack to keep track of the opening brackets encountered.
        stack = []

        # Next, we use a loop that will go through each character.
        for char in s:
            # If the character is a closing bracket, it will then check whether the stack is empty or if the top of the stack matches the corresponding opening bracket.
            # If the character is an opening bracket, it pushes it onto the stack.
            if char in matching_bracket:
                top_element = stack.pop() if stack else '#'
                if matching_bracket[char] != top_element:
                    return False
            else:
                stack.append(char)

        # After the loop, if the stack is empty, all brackets are matched correctly, so the function returns True and vice versa.
        return not stack