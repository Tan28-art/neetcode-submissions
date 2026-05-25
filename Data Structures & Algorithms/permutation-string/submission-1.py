class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        hashMaps1 = {}
        hashMaps2 = {}
        left = 0
        right = 0
        
        # Initialize hash maps
        for i in range(ord('a'), ord('z') + 1):
            hashMaps1[chr(i)] = 0
            hashMaps2[chr(i)] = 0

        # Fill hash map for s1
        for char in s1:
            hashMaps1[char] += 1

        # Initialize the window with the first len(s1) characters of s2
        while right < len(s1):
            hashMaps2[s2[right]] += 1
            right += 1

        # Check if the initial window matches
        if hashMaps1 == hashMaps2:
            return True

        # Slide the window across s2
        while right < len(s2):
            # Add the new character to the window
            hashMaps2[s2[right]] += 1
            # Remove the character that's no longer in the window
            hashMaps2[s2[left]] -= 1
            
            # Move the window
            left += 1
            right += 1
            
            # Check if the current window matches
            if hashMaps1 == hashMaps2:
                return True

        return False