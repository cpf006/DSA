# https://leetcode.com/problems/binary-search/
# My solution:

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        mid = (high + low) // 2
        
        while high != low:
            mid = (high + low) // 2
            if nums[mid] == target:
                break
            elif nums[mid] < target:
                low = mid + 1
                mid = mid + 1
            else:
                high = mid
    
        if nums[mid] == target:
            return mid
        else:
            return -1

# Based on checking this gif:
#     https://blog.penjee.com/binary-vs-linear-search-animated-gifs/

# Reasoning:
#     Because we know the mid point is less than we can skip over the mid point when increasing low,
#         because // 2 will return the floor of the division
#         1 + 2 // 2 will return 1, we need to make the low point the same as high to do the final check if it gets to that point.
        
#         once checked, the final if statement checks if at that midpoint it does infact equal target.
#         ..


# Slightly improved (still mine):
# Returning mid as soon as its found vs breaking and checking a second time.
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        mid = (high + low) // 2
        
        while high != low:
            mid = (high + low) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
                mid = mid + 1
            else:
                high = mid
    
        if nums[mid] == target:
            return mid
        else:
            return -1

# Suprisingly slightly slower(still mine):
# this attempts to move the window slightly in more each itteration.
# I believe this is slightly longer given the additional update to the high value
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        mid = (high + low) // 2
        
        while high > low:
            mid = (high + low) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid = mid + 1
            else:
                high = mid = mid - 1
    
        if nums[mid] == target:
            return mid
        else:
            return -1

# Test cases:
# [-1,0,3,5,9,12]
# 9
# [-1,0,3,5,9,12]
# -1
# [-1,0,3,5,9,12]
# 12
# [-1,0,3,5,9,12]
# 2
# [2,5]
# 0

# Discussion best solution:
class Solution:
    def search(self, nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                return mid
        return -1

# Because we are using <= and right is also decrimenting
# by 1, we don't have to worry about setting mid again?

