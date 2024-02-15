class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        nums.sort(reverse=True)
        for n in range(1, len(nums)):
            n_nums = nums[n:]
            l_num = nums[n-1]
            if sum(n_nums) > l_num:
                if len(n_nums) + 1 > 2:
                    return sum(n_nums) + l_num
                else:
                    return -1
        return -1
