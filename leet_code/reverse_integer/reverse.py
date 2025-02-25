class Solution:
    def reverse(self, x: int) -> int:
        mult = 1 if x >= 0 else -1
        new_x = abs(x)
        number = 0
        res = []
        while new_x >= 1:
            rem = new_x % 10
            res.append(rem)
            new_x = new_x // 10
        exp = len(res) - 1
        for index, value in enumerate(res):
            number += value * 10 ** (exp - index)
        limit = 2**31
        number = mult * number
        if (number <= -limit) or (number > limit - 1):
            return 0
        return number
