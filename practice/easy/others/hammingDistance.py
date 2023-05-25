class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        z = x ^ y

        binary = []
        while z != 0:
            binary.append(z % 2)
            z = z // 2

        return binary.count(1)
