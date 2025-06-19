class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_found = {}
        n = len(nums)

        for i in range(n):
            num2 = target - nums[i]
            if num2 in nums_found:
                return [nums_found[num2], i]
            nums_found[nums[i]] = i
        
        return []

                
