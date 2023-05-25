from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        new_strs = ["".join(sorted(list(x))) for x in strs]

        parse = defaultdict(list)

        for i in range(len(strs)):
            parse[new_strs[i]].append(strs[i])

        result = []
        for _, val in parse.items():
            result.append(val)

        return result
