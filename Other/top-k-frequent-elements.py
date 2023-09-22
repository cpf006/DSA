# My first solution. While this works it seems it may be better to make the sorting manually 
# or possibly use a heap
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}

        for num in nums:
            if num not in counts: counts[num] = 0
            counts[num] += 1
        
        return sorted(counts, key=counts.get, reverse=True)[:k]
