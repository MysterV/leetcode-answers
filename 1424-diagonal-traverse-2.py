class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        n_cols = max(len(i) for i in nums)
        n_rows = len(nums)
        distances = {i:list() for i in range(n_rows+n_cols-1)}
        for i in range(n_rows):
            for j in range(len(nums[i])):
                distances[i+j].append(nums[i][j])

        return [distances[i][j] for i in range(len(distances)) for j in range(len(distances[i])-1, -1, -1)]