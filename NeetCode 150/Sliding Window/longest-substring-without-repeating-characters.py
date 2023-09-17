#https://leetcode.com/problems/longest-substring-without-repeating-characters/
# My first solution
class Solution:    
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1: return len(s)        
        non_repeating = ''
        max_non_repeating_len = 0

        for i in range(len(s)):
            if s[i] in non_repeating:
                if len(non_repeating) > max_non_repeating_len:
                    max_non_repeating_len = len(non_repeating)
                
                left = non_repeating.find(s[i]) + 1
                right = len(non_repeating)
                non_repeating = non_repeating[left:right]
            non_repeating += s[i]
            
        if len(non_repeating) > max_non_repeating_len:
            return len(non_repeating)
        else:
            return max_non_repeating_len


'''
Hint for next time:
Think of using a hash table 
(only one character can exist in keys at a time)
you only need to know the start of the non repeating to the current
i index of where you see a repeating character
'''
        