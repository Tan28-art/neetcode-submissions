class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        count_left = 1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                # you can delete at either left or right
                # delete left
                left += 1
                count_left -= 1
                
        left = 0
        right = len(s) - 1
        count_right = 1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                # you can delete at either left or right
                # delete right
                right -= 1
                count_right -= 1

        if count_left >= 0 or count_right >= 0:
            return True
        return False