class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        numbers = {nums[i]:i for i in range(len(nums))}
        for i in range(len(nums)):
            j = target-nums[i]
            if j in numbers and numbers[j] != i:
                return [i, numbers[j]]
        return []