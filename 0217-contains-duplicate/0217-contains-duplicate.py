class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        hash_map = {}
        for i in range(len(nums)):
            hash_map[nums[i]] = hash_map.get(nums[i],0) +1
        for i in hash_map:
            if hash_map[i] > 1:
                return True
            
        return False
        