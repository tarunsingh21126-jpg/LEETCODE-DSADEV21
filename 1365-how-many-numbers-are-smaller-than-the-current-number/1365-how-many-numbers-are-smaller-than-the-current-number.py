class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        n = len(nums)
        new = sorted(nums)
        listans = {}
        for i in range(n):
            if new[i] not in listans:
                listans[new[i]] = i
        ans = []

        for i in range(len(nums)):
            ans.append(listans[nums[i]])
        return ans

        