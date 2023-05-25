import math


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join([i.lower() for i in s if i.isalnum()])
        if s == "" or len(s) == 1:
            return True

        return s[:len(s) // 2] == (s[math.ceil(len(s) / 2):])[::-1]
