class Solution:
    # def isPalindrome(self, s: str) -> bool:
    #     # s = ''.join([i.lower() for i in s if i.isalnum()])
    #     if s == "" or len(s) == 1:
    #         return True
    #
    #     return s == s[::-1]
    #
    # def longestPalindrome(self, s: str) -> str:
    #     max_pal = ""
    #
    #     for i in range(len(s)):
    #         for j in range(len(s), i, -1):  # j = end, O = n^2
    #             if len(max_pal) >= j - i:  # To reduce time
    #                 break
    #             if self.isPalindrome(s[i:j]):
    #                 max_pal = s[i:j]
    #
    #     return max_pal

    def longestPalindrome(self, s: str) -> str:
        if s is "":
            return s
        dp = [[None for _ in range(len(s))] for _ in range(len(s))]

        res = ""

        for j in range(len(s)):
            for i in range(j + 1):
                if i == j:
                    dp[i][j] = True
                elif j == i + 1 and s[i] == s[j]:
                    dp[i][j] = True
                else:
                    if dp[i + 1][j - 1] and s[i] == s[j]:
                        dp[i][j] = True

                if dp[i][j] and j - i + 1 > len(res):
                    res = s[i:j + 1]

        return res
