NO_OF_CHAR = 123

class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = [0] * NO_OF_CHAR
        for ch in s:
            count[ord(ch)] += 1

        for i in range(len(s)):
            if count[ord(s[i])] == 1:
                return i

        return -1