class Solution:
    def isAlphaNumeric(self, c) -> bool:
        if ("a" <= c.lower() <= "z") or ("0" <= c <= "9"):
            return True
        else:
            return False

    def isPalindrome(self, s: str) -> bool:
        leftPointer = 0
        rightPointer = len(s) - 1

        while leftPointer < rightPointer:
            while leftPointer < rightPointer and not self.isAlphaNumeric(s[leftPointer]):
                leftPointer += 1

            while leftPointer < rightPointer and not self.isAlphaNumeric(s[rightPointer]):
                rightPointer -= 1

            if s[leftPointer].lower() != s[rightPointer].lower():
                return False
            
            leftPointer += 1
            rightPointer -= 1
        
        return True
         