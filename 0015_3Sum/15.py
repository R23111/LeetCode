class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        tri = []
        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                for k in range(j+1, len(nums)):
                    l = [nums[i],nums[j],nums[k]]
                    if (sum(l) == 0):
                        l = sorted(l)
                        if not l in tri:
                            tri.append(l)    

        return tri