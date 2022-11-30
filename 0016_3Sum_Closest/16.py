class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        lng = len(nums)

        closest = None

        for i in range(lng - 2):
            j, k = i+1, lng - 1
            while j < k:
                s = sum([nums[i], nums[j], nums[k]])
                if s == target:
                    return s

                if (closest is None) or (abs(s - target) < abs(closest - target)):
                    closest = s

                if s < target:
                    j += 1
                elif s > target:
                    k -= 1

        return closest
