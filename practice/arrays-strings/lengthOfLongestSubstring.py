class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_index = {}
        start = 0
        max_len = 0

        for i in range(len(s)):
            if s[i] in last_index.keys():
                start = max(start, last_index[s[i]] + 1)

            max_len = max(max_len, i - start + 1)
            last_index[s[i]] = i

        return max_len
