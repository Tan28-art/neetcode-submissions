class Solution:
    def isAplhaNum(self, char):
        return (("a" <= char <= "z") or ("A" <= char <= "Z") or ("0" <= char <= "9"))
    
    def isPalindrome(self, string):
        n = len(string) - 1
        
        left = 0
        right = n

        while left < right:
            while left < right and not self.isAplhaNum(string[left]):
                left += 1

            while left < right and not self.isAplhaNum(string[right]):
                right -= 1

            if string[left].lower() != string[right].lower():
                return False
            
            left += 1
            right -= 1

        return True
