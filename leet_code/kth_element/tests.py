class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.nums = nums.copy()
        self.nums.sort(reverse=True)
        self.nums = nums[:k][::-1]
        self.k = k
        print(f"Init: {self.nums}")

    def add(self, val: int) -> int:
        print(self.nums)
        if self.nums[-1] >= val:
            return self.nums[self.k - 1]
        pos_swap = 0
        for index, num in enumerate(self.nums):
            if val >= num:
                pos_swap = index
                break
        self.nums.insert(pos_swap, val)
        self.nums.pop(-1)
        return self.nums[-1]
