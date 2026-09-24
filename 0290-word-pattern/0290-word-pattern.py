class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        list_ans = []
        hash_map = {}

        word = []
        wordmap = {}

        for i in range(len(pattern)):
            if pattern[i] not in hash_map:
                hash_map[pattern[i]] = i

            list_ans.append(hash_map[pattern[i]])

        for i in range(len(words)):
            if words[i] not in wordmap:
                wordmap[words[i]] = i

            word.append(wordmap[words[i]])

        for i in range(len(pattern)):
            if list_ans[i] != word[i]:
                return False

        return True

        
                