class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(s) -> bool:
            left, right = 0, len(s) - 1
            while left < right:
                if s[left] != s[right]:
                    return False
            
                left += 1
                right -= 1
            return True
        
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                # first mismatch
                # remove either left or rigth and check
                return is_palindrome(s[left+1:right+1]) or is_palindrome(s[left:right])

            left += 1
            right -= 1
        return True
