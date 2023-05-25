class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        n = len(s)
        i = 0

        while i < n:
            if s[i] == "I":
                result += 1
                i += 1
                if i < n:
                    if s[i] == "V":
                        result += 3
                        i += 1
                    elif s[i] == "X":
                        result += 8
                        i += 1
                continue

            if s[i] == "V":
                result += 5
                i += 1
                continue

            if s[i] == "X":
                result += 10
                i += 1
                if i < n:
                    if s[i] == "L":
                        result += 30
                        i += 1
                    elif s[i] == "C":
                        result += 80
                        i += 1
                continue

            if s[i] == "L":
                result += 50
                i += 1
                continue

            if s[i] == "C":
                result += 100
                i += 1
                if i < n:
                    if s[i] == "D":
                        result += 300
                        i += 1
                    elif s[i] == "M":
                        result += 800
                        i += 1
                continue

            if s[i] == "D":
                result += 500
                i += 1
                continue

            if s[i] == "M":
                result += 1000
                i += 1
                continue

        return result
