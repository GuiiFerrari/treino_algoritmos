class Solution:
    def singleNonDuplicate(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if (mid == 0 or nums[mid] != nums[mid - 1]) and (
                mid == len(nums) - 1 or nums[mid] != nums[mid + 1]
            ):
                return nums[mid]
            if (mid % 2) == 0:
                if mid + 1 < len(nums) and nums[mid] == nums[mid + 1]:
                    left = mid + 2
                else:
                    right = mid - 1
            else:
                if nums[mid - 1] == nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
        return nums[left]
