class Solution:
    def maxArea(self, heights):
        
        area = 0
        left = 0
        right = len(heights) - 1

        while left < right:
            new_area = (right - left) * min(heights[left], heights[right])
            if new_area > area:
                area = new_area

            if heights[left] >  heights[right]:
                right -= 1

            elif heights[right] >=  heights[left]:
                left += 1
            
            
        
        return area

