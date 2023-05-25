class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0

        result = []
        if s[0] == "-" or s[0] == "+":
            result.append(s[0])
            s = s[1:]

        for ch in s:
            if ch.isnumeric():
                result.append(ch)
            else:
                break

        if not result or result == ["-"] or result == ["+"]:
            return 0

        result = int("".join(result))

        return -2147483648 if -2147483648 > result else 2147483647 if result > 2147483647 else result