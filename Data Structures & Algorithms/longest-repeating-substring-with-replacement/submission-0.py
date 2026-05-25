class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashMap = {}
        left = 0
        right = 0
        result = 0
 
        while right < len(s):
            hashMap[s[right]] = 1 + hashMap.get(s[right], 0)
            

            while (right - left + 1) - max(hashMap.values()) > k:
                hashMap[s[left]] -= 1
                left += 1

            if result < (right - left + 1):
                result = (right - left + 1)
                
            right += 1
        
        return result
