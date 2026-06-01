class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # merge sort ig
        
        n = len(nums)
        
        def merge(arr, l, m, r):
            left = arr[l : m+1]
            right = arr[m+1 : r+1]

            i, p1, p2 = l, 0, 0

            while p1 < len(left) and p2 < len(right):
                if left[p1] < right[p2]:
                    arr[i] = left[p1]
                    p1 += 1
                    
                else:
                    arr[i] = right[p2]
                    p2 += 1
                
                i += 1

            while p1 < len(left):
                arr[i] = left[p1]
                i += 1
                p1 += 1

            while p2 < len(right):
                arr[i] = right[p2]
                i += 1
                p2 += 1


        
        def merge_sort(arr, l, r):
            if l == r:
                return arr
            
            mid = (l+r)//2
            # left half
            merge_sort(arr, l, mid)
            # right
            merge_sort(arr, mid + 1, r)
            
            merge(arr, l, mid, r)

            return arr

        return merge_sort(nums, 0, n-1)
        
            
