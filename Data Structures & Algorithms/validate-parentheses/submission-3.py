class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashMap = {")":"(", "}":"{", "]":"["}

        for char in s:
            # pushing into stack
            # opening parenthesis
            if char not in hashMap:
                stack.append(char)

            # closing parenthesis 
            else:
                print(stack)
                if stack != [] and hashMap[char] == stack[-1]  :
                    stack.pop()
                    
                # mismatch found
                else:
                    return False

        if stack == []:
            return True
        
        return False
