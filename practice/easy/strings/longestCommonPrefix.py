from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = []
        strs = zip(*strs)

        for x in strs:
            if len(set(x)) == 1:
                result.append(x[0])
            else:
                break

        return "".join(result)




