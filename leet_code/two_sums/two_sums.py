class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(0, len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if sum(nums[i : j + 1]) == target:
                    return list(range(i, j + 1))


# class Solution:
#     def twoSum(self, nums: list[int], target: int) -> list[int]:
#         ordered_nums = nums.copy()
#         ordered_nums.sort()
#         ordered_order = list(range(len(nums)))
#         ordered_order.sort(key=lambda x: nums[x])
#         cum_sum = [sum(ordered_nums[: i + 1]) for i in range(len(ordered_nums))]
#         answer = -1
#         for index in range(len(cum_sum)):
#             if cum_sum[index] == target:
#                 answer = index
#                 break
# return ordered_order[:answer]
