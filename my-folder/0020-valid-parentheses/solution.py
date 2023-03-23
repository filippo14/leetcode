class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        chars = {")": "(", "]": "[", "}": "{", "(": ")", "[": "]", "{": "}"}
        stack = []


        for ele in s:

            if ele == "(" or ele == "[" or ele == "{":
                stack.append(ele)

            else:
                if len(stack) == 0:
                    return False
                lastOpenParenthes = stack.pop() 
                if lastOpenParenthes != chars[ele]:
                    return False

        if len(stack) != 0:
            return False

        return True
        
