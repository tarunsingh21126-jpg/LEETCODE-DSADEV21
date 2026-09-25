class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        hashmap = {}
        ans = []
        if len(nums1) <= len(nums2):
            small = nums1
            large = nums2
        else:
            small = nums2
            large = nums1
        for x in small:
            hashmap[x] = hashmap.get(x, 0) + 1
        for x in large:
            if x in hashmap and hashmap[x] > 0:
                ans.append(x)
                hashmap[x] -= 1
        return ans
        



        

        