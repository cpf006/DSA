# https://leetcode.com/problems/valid-anagram
# My solution:
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        letters_used = {}
        for index in range(len(s)):
            if s[index] in letters_used:
                letters_used[s[index]] += 1
            else:
                letters_used[s[index]] = 1
                
            if t[index] in letters_used:
                letters_used[t[index]] -= 1
            else:
                letters_used[t[index]] = -1
                
        return all(val == 0 for val in letters_used.values())

# Improved cleaner solutions:
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT
        