class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        hashmap = {}
        for x in t:
            hashmap[x] = hashmap.get(x,0) +1
        for x in s:
            hashmap[x] -= 1
        for x in hashmap:
            if hashmap[x] > 0:
                return x

            