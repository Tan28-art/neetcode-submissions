class Solution:
    def isPalindrome(self, s: str) -> bool:
        #removing all the unnecessary stuff from the string
        string = ""
        for i in range(len(s)):
            if ( (s[i].lower() >= "a") and (s[i].lower() <= "z") ) or ( (s[i] >= "0") and (s[i] <= "9") ):
                string = string + s[i].lower()
        
        # print(string)
        
        str_reverse = ""
        for i in range(len(string)-1, -1, -1):
            str_reverse += string[i]
            
        if string == str_reverse:
            return True
        else:
            return False