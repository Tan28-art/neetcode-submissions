class Solution:
    def maxArea(self, heights):
        
        area = 0
        
        for i in range(len(heights)):
            
            for j in range(i+1, len(heights)):
                
                new_area = min(heights[i], heights[j]) * (j - i)

                if new_area > area:
                    area = new_area
                
            
            
        
        return area

