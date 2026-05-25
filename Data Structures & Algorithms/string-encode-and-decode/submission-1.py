from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        final_str = ""
        
        for i in range(len(strs)):
            length = str(len(strs[i]))
            delimiter = "$"
            strs[i] = length + delimiter + strs[i]
            
        for i in strs:
            final_str += i
            
        return final_str
    
    def decode(self, s: str) -> List[str]:
        final_array = []
        i = 0

        while i < len(s):
            length_str = ""
            
            while s[i] != "$":
                length_str += s[i]
                i += 1
            
            length_int = int(length_str)
            i += 1  
            
            
            final_array.append(s[i:i + length_int])
            i += length_int

        return final_array
