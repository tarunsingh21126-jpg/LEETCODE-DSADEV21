class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        hash_map ={}
        for i in range(len(nums)):
            hash_map[nums[i]] = hash_map.get(nums[i],0) +1
        for i in hash_map:
            if hash_map[i] > len(nums)/2 :
                return i 