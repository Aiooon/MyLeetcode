import math


class Solution:
    def cuttingRope(self, n: int) -> int:
        if n < 2:
            return 0
        elif n == 2:
            return 1
        elif n == 3:
            return 2
        store = [0 for i in range(0, n + 1)]
        store[0], store[1], store[2], store[3] = 0, 1, 2, 3
        for i in range(4, n + 1):
            max = 0
            for j in range(1, (i // 2) + 1):
                temp = store[j] * store[i-j]
                if max < temp:
                    max = temp
                store[i] = max
        return store[n]

    def _cuttingRope(self, n: int) -> int:
        if n <= 3:
            return n - 1
        a, b = n // 3, n % 3
        if b == 0:
            return int(math.pow(3, a))
        if b == 1:
            return int(math.pow(3, a - 1) * 4)
        return int(math.pow(3, a) * 2)


print(Solution().cuttingRope(10))


