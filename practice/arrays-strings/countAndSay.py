class Solution:
    def countAndSay(self, n: int) -> str:
        parse = {1: "1"}

        for i in range(2, n + 1):
            previous = parse[i - 1]
            previous = list(previous)
            new = []

            curr = 0
            prev = 0
            curr_count = 0

            while curr < len(previous):
                while curr < len(previous) and previous[curr] == previous[prev]:
                    curr_count += 1
                    curr += 1

                new.append(str(curr_count))
                new.append(str(previous[prev]))

                prev = curr
                curr_count = 0

            parse[i] = "".join(new)

        return parse[n]
