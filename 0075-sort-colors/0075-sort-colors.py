class Solution:
    def sortColors(self, nums: list[int]) -> None:
        n = len(nums)
        for i in range(n-1):
            mindx = i
            for j in range(i + 1, n):
                if nums[j] < nums[mindx]:
                    mindx = j
            if mindx != i:
                nums[i], nums[mindx] = nums[mindx], nums[i]
        return nums


        