class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mean = left + ((right - left) // 2)  

            if nums[mean] > target:
                right = mean - 1
            elif nums[mean] < target:
                left = mean + 1
            else:
                return mean
        return -1
