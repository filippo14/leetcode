class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # defaultdict automatically creates an empty list if the key doesn't exist 
        anagrams = defaultdict(list)

        for str in strs:
            # sorting the string alphabetically and the characters are joined back to form a new string
            # that will be the reference for anagrams
            ref_str = "".join(sorted(str))

            # appending the string to the list in the dict corresponding to the reference of the anagrams.
            anagrams[ref_str].append(str)
        
        return list(anagrams.values())

# Time complexity: O(m * nlogn)
# Space complexity: O(mn)


