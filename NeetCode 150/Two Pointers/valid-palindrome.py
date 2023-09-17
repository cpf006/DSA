# https://leetcode.com/problems/valid-palindrome/
# My Solution
class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha_only = ''.join(c for c in s if c.isalnum())
        cleaned_s = alpha_only.lower()
        for i in range(len(cleaned_s)//2):
            if cleaned_s[i] != cleaned_s[(len(cleaned_s) - 1 - i)]:
                return False
        return True

# Faster and less memory method
'''
    This method skips non alpha numaric and compares 
    case for each character instead of cleaning the string
    beforehand
'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            if not s[l].isalnum():
                l += 1
            elif not s[r].isalnum():
                r -= 1
            else:
                if s[l].lower() != s[r].lower():
                    return False
                else:
                    l += 1
                    r -= 1
        return True
