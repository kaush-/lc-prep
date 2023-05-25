class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for ch in s:
            if ch in ["(", "[", "{"]:
                stack.append(ch)
                continue

            if ch in [")", "]", "}"] and len(stack) == 0:
                return False

            if (ch == ")" and stack[-1] != "(") or (ch == "]" and stack[-1] != "[") or (ch == "}" and stack[-1] != "{"):
                return False

            stack.pop()

        return len(stack) == 0
