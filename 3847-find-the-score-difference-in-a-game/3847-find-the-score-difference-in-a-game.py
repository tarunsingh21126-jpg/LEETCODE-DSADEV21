

class Solution:
    def scoreDifference(self, nums: List[int]) -> int:
        score1 = 0
        score2 = 0
        active = 0  # 0 = first player, 1 = second player

        for i in range(len(nums)):

            # Swap if nums[i] is odd
            if nums[i] % 2 == 1:
                active ^= 1

            # Swap every 6th game (index 5, 11, 17, ...)
            if i % 6 == 5:
                active ^= 1

            # Add score to active player
            if active == 0:
                score1 += nums[i]
            else:
                score2 += nums[i]

        return score1 - score2