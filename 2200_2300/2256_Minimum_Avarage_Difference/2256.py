class Solution:
    def minimumAverageDifference(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return 0

        s2 = sum(nums[1:])
        l2 = len(nums)-1
        s1 = nums[0]
        l1 = 1

        min_diff = abs(s1//l1 - s2//l2)
        if min_diff == 0:
            return 0
        idx = 0

        for i in range(1, len(nums)):

            s1 += nums[i]
            s2 -= nums[i]
            l1 += 1
            l2 -= 1
            if l2 == 0:
                l2 = 1

            diff = abs(s1//l1 - s2//l2)

            if diff == 0:
                return i
            elif diff < min_diff:
                min_diff = diff
                idx = i

        return idx
