class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        hashmap = {}
        used_words = set()
        for i in range(len(pattern)):
            char = pattern[i]
            word = words[i]
            if char in hashmap:
                if hashmap[char] != word:
                    return False
            else:
                if word in used_words:
                    return False
                hashmap[char] = word
                used_words.add(word)
        return True
