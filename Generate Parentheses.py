"""
Problem:
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 

Constraints:

1 <= n <= 8
"""

class Solution(object):
    def generateParenthesis(self, n):
        """
        First, we need to create a backtracking function. 
        The logic here is that we will create the string of parentheses step-by-step, ensuring that in every step, the string is valid. 
        The code uses recursion to explore all possible combinations and the code also keeps track of the number of open and closed parentheses used so far which ensures that the string remains valid.
        """
        def backtrack(S, left, right):
            """
            Next, we have a base case of the length of the current string ‘S’ which is equal to ‘2 *n’. 
            This means that we have formed a valid string of ‘n’ pairs of parentheses, so we add it to the result list and return.
            """
            if len(S) == 2 * n:
                result.append(S)
                return
            # Next, using recursions, we can count if the number of open parentheses used is less than n. we can then recall the updated values afterward. Same goes for the closed parentheses.
            if left < n:
                backtrack(S + '(', left + 1, right)
            if right < left:
                backtrack(S + ')', left, right + 1)

        """
        Lastly, we initialize the result list to store all valid combinations of parentheses. 
        We also start the backtracking process by calling backtrack with an empty string and 0 for both left and right. 
        Then we return the result list.
        """
        result = []
        backtrack('', 0, 0)
        return result