class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1

        while left <= right:
            mid = left + ((right - left) // 2)
            left_inner = 0
            right_inner = len(matrix[mid]) - 1

            if target == matrix[mid][left_inner] or target == matrix[mid][right_inner]:
                return True

            elif matrix[mid][left_inner] < target < matrix[mid][right_inner]:
                break

            elif target < matrix[mid][left_inner]:
                right = mid - 1

            else:
                left = mid + 1

        

        left_inner = 0
        right_inner = len(matrix[mid]) - 1
        while left_inner <= right_inner:
            mid_inner = left_inner + ((right_inner - left_inner) // 2)

            if target == matrix[mid][mid_inner]:
                return True
            
            elif target < matrix[mid][mid_inner]:
                right_inner = mid_inner - 1

            else:
                left_inner = mid_inner + 1
        
        return False


            
