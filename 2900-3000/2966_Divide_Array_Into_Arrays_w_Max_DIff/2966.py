class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        if len(nums)%3:
            return []
        nums.sort()
        arrays = []
        a = 0
        for i in range(0, len(nums), 3):
            if nums[i+2] - nums[i] > k:
                return []
            arrays.append([nums[i], nums[i+1], nums[i+2]])

        return arrays

