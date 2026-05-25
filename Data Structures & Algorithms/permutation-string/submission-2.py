class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        

        if len(s1) > len(s2):
            return False
        
        else:
            hashMaps1 = {}
            hashMaps2 = {}
            left = 0
            right = 0
            #filling up s1 hashMap
            
            for i in range(ord('a'), ord('z') + 1):
                hashMaps1[chr(i)] = 0
                hashMaps2[chr(i)] = 0
                
            for char in s1:
                hashMaps1[char] += 1

            # main loop
            while right < len(s1):
                hashMaps2[s2[right]] += 1
                right += 1 

            while right < len(s2):
                if hashMaps1 == hashMaps2:
                    return True

                else:
                    hashMaps2[s2[left]] -= 1
                    hashMaps2[s2[right]] += 1
                    left += 1
                    right += 1
                    
            #check last window
            if hashMaps1 == hashMaps2:
                return True
                
            return False



                