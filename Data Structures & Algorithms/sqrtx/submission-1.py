class Solution:
    def mySqrt(self, x: int) -> int:
        # think about it, you probably need to 
        # find the closest value that results in 
        # sqrt
        # so for a number like 13, its between 3^2 and 4^2
        # Number is non negative, so from 2 onwards, you can just 
        # cut half the search space, for 13 you do not need to check 7 
        # and above

        left = 0
        right = x//2

        while left <= right:
            if x == 0 or x == 1:
                return x
            mid = (left + right) // 2
            sqr = mid * mid
            sqr1 = (mid + 1) * (mid + 1)
            # sqr < x < sqr1
            if sqr < x and x < sqr1:
                return mid
            elif sqr == x:
                return mid
            elif sqr > x:
                right = mid-1
            else:
                left = mid + 1



        