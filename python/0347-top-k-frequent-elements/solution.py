class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        repetitions = {}
        for num in nums:
            if num in repetitions:
                repetitions[num] += 1
            else:
                repetitions[num] = 1
        
        return [key for key, _ in sorted(repetitions.items(), key=lambda item: item[1], reverse=True)[:k]]
