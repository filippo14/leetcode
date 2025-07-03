class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # Constraints: -5 * 10^4 <= nums[i] <= 5 * 10^4
        # Use counting sort since range is limited

        def counting_sort():
            minVal, maxVal = min(nums), max(nums)  # Step 1: determine range
            offset = -minVal  # To shift negative values to index 0
            count = [0] * (maxVal - minVal + 1)  # Step 2: count array sized to cover full range

            for val in nums:  # Step 3: count occurrences
                count[val + offset] += 1

            index = 0
            for val in range(minVal, maxVal + 1):  # Step 4: write back sorted values
                while count[val + offset] > 0:
                    nums[index] = val
                    index += 1
                    count[val + offset] -= 1

        counting_sort()
        return nums

