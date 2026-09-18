class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        left = 0
        ans = []

        while left < n:
            right = left + 1
            count = 1

            ans.append(nums[left])

            while right < n and count < k:
                if nums[left] == nums[right]:
                    ans.append(nums[right])
                    count += 1
                    right += 1
                else:
                    break

            while right < n and nums[right] == nums[left]:
                right += 1

            left = right

        return ans

                


