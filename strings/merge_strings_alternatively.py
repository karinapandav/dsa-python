"""
LeetCode 1768 - Merge Strings Alternately

Problem:
Merge two strings by alternating characters.
If one string is longer, append the remaining characters.

Example:
Input:
word1 = "abc"
word2 = "pqr"

Output:
"apbqcr"
"""
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = []
        i = 0

        while i < len(word1) and i < len(word2):
            ans.append(word1[i])
            ans.append(word2[i])
            i += 1

        while i < len(word1):
            ans.append(word1[i])
            i += 1

        while i < len(word2):
            ans.append(word2[i])
            i += 1

        return "".join(ans)
        
        while l1p < len(l1):
            ans= ans + l1[l1p]
            l1p+=1
            
        while l2p < len(l2):
            ans = ans + l2[l2p]
            l2p+=1
        
        return ans
