class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count_s, count_t = {}, {}

        for idx in range(len(s)):
            count_s[s[idx]] = 1 + count_s.get(s[idx], 0)
            count_t[t[idx]] = 1 + count_t.get(t[idx], 0)

        return count_s == count_t
