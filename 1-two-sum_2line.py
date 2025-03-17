class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        ns = {nums[i]:i for i in range(len(nums))}
        return [(i,ns[target-nums[i]]) for i in range(len(nums)) if target-nums[i] in ns and ns[target-nums[i]] != i][0]