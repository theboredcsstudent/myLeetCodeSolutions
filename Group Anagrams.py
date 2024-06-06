"""
Problem:
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
 

Constraints:

1 <= strs.length <= 10^4
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""

# First, we will import defaultdict as it will give us the ability to use the defaultdict function.
from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        # Next, we then initialize a variable named anagrams which is equal to defaultdict(list), this will give us the ability to access or modify a key that doesn’t exist in the dictionary.
        anagrams = defaultdict(list)

        """
        Next, we need to run through each character in the strs input so we do that by doing a for loop, 
        we sort each character using sorted(s) which returns a list of characters and then we join these characters back into a string using ‘’.join(sorted(s)). 
        This way, the sorted string is used as the key, and our original string is appended to the list of anagrams for that key.
        """
        for s in strs:
            sorted_str = ''.join(sorted(s))
            anagrams[sorted_str].append(s)
            
        # Lastly, we return the values of the dictionary as a list using list(anagrams.values())
        return list(anagrams.values())