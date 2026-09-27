class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = {}
        t = []
        for i in range(len(s)):
            if s[i] not in t:
                t.append(s[i])
            else:
                hashmap[''.join(t)] = len(t)
                t = t[t.index(s[i]) + 1:] + [s[i]]
        if t:
            hashmap[''.join(t)] = len(t)
        return max(hashmap.values()) if hashmap else 0
            



       
        
        