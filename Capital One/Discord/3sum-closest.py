#https://leetcode.com/problems/3sum-closest/
# My solution ( After checking discussion )
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum = sum(nums[:3])
        for i in range(len(nums)):
            left, right = 0, len(nums) - 1
            while left < right:
                if i == left:
                    left += 1
                    continue
                if i == right:
                    right -= 1
                    continue
                    
                current_sum = nums[i] + nums[left] + nums[right]
                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    return target #found target sum

                if(abs(current_sum - target) < abs(closest_sum - target)):
                    closest_sum = current_sum
            
        return closest_sum

# Discussion solution
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = nums[0] + nums[1] + nums[2]
        for i in range(len(nums)-2):

            # update: ignore the duplicate numbers
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                curSum = nums[l] + nums[r] + nums[i]
                if curSum == target:
                    return target
                if abs(curSum-target) < abs(result-target):
                    result = curSum
                if curSum < target:
                    l += 1
                else:
                    r -= 1
        return result