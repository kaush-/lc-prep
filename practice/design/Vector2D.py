from collections import deque
from typing import List


class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.queue = deque()
        for lst in vec:
            for ele in lst:
                self.queue.append(ele)

    def next(self) -> int:
        return self.queue.popleft()

    def hasNext(self) -> bool:
        return True if len(self.queue) else False

# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()
