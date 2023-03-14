class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        ele_found = set()
        for i in nums:
            if i in ele_found:
                return True
            ele_found.add(i)
        return False
