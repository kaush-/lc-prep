import random
from collections import defaultdict


class RandomizedSet:

    def __init__(self):
        self.lst = defaultdict(int)
        self.count = 0

    def insert(self, val: int) -> bool:
        if self.lst[val]:
            return False

        self.lst[val] += 1
        self.count += 1
        return True

    def remove(self, val: int) -> bool:
        if not self.lst[val]:
            del self.lst[val]
            return False

        del self.lst[val]
        self.count -= 1
        return True

    def getRandom(self) -> int:
        print(list(self.lst.keys()))
        rand_int = random.choice(list(self.lst.keys()))
        return rand_int

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
