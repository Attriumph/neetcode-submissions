class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) <= 1: return []

        num_map = {}
        for i in range(len(nums)):
            num_map[nums[i]] = i

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in num_map and num_map[diff] != i:
                return [i, num_map[diff]]
        
        return []
        