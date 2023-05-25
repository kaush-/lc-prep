NO_OF_CHAR = 123

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = [0] * NO_OF_CHAR
        for ch in s:
            count[ord(ch)] += 1

        for ch in t:
            count[ord(ch)] -= 1

        for i in range(NO_OF_CHAR):
            if count[i] != 0:
                return False

        return True