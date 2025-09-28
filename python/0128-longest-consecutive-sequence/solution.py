class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest_seq = 0
        sequence = 0

        for num in nums_set:
            # checking if it is a sequence
            if (num - 1) not in nums_set:
                sequence = 1
                while (num + sequence) in nums_set:
                    sequence += 1
            
            longest_seq = max(sequence, longest_seq)

        return longest_seq

