class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()

        left = 0
        right = len(nums) - 1
        k = -1

        while left < right:

            if nums[left] + nums[right] == 0:
                k = max(k, nums[right])
                left += 1
                right -= 1

            elif abs(nums[left]) > nums[right]:
                left += 1

            else:
                right -= 1

        return k