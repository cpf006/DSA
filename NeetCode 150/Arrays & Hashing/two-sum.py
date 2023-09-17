#https://leetcode.com/problems/two-sum/

# Brute Force:
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx_one in range(len(nums)):
            for idx_two in xrange(len(nums)):
                if idx_one != idx_two:
                    if (nums[idx_one] + nums[idx_two]) == target:
                        return [idx_one, idx_two]

# Improved solution:
class Solution:
   def twoSum(self, nums: List[int], target: int) -> List[int]:
       seen = {}
       for i, value in enumerate(nums):
           remaining = target - nums[i]
           
           if remaining in seen:
               return [i, seen[remaining]]
           else:
               seen[value] = i