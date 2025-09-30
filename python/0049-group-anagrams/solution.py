class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # sorting the list requires O(nlogn), we can do better with an hash table --> O(m * n) with m the number of strings in strs and n is the length of the longest string.

        output = defaultdict(list)
        
        for s in strs:
            count = [0] * 26 
            for letter in s:
                count[ord(letter) - ord("a")] += 1
            output[tuple(count)].append(s)

        return list(output.values())

