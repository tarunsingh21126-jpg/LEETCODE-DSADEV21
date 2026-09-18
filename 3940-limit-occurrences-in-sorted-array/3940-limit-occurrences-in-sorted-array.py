class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        left = 0
        right = 0

        while right < n:

            count = 0
            current = nums[right]

            while right < n and nums[right] == current:
                if count < k:
                    nums[left] = nums[right]
                    left += 1
                    count += 1

                right += 1

        return nums[:left]