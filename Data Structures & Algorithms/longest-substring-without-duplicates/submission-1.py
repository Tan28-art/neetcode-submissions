class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        left = 0
        right = 0
        length = 0

        while right < len(s):
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1
            
            charSet.add(s[right])
            lengthWindow = right - left + 1

            if lengthWindow > length:
                length = lengthWindow

            right += 1

        return length
