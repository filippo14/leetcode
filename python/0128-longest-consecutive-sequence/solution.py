class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_ordered = sorted(nums)
        longest_seq = 1
        sequence = 1

        if not nums_ordered:
            return 0

        for i in range(len(nums_ordered)-1):
            if nums_ordered[i] == nums_ordered[i+1] - 1:
                sequence += 1
            elif nums_ordered[i] != nums_ordered[i+1]: # not consecutive
                sequence = 1
            if sequence > longest_seq:
                longest_seq = sequence
            continue
        
        return longest_seq
