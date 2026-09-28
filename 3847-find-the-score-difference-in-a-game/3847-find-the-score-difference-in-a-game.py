class Solution:
    def scoreDifference(self, nums: List[int]) -> int:
        score1,score2 = 0,0
        act = 0
        for i in range(len(nums)):
            if (nums[i] % 2) == 1:
                act = 1 - act
            if (i+1) % 6 == 0:
                act = 1 - act
            if act == 0:
                score1 += nums[i]
            else:
                score2 += nums[i]

        return score1 - score2
                


            


