class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        a = len(word1)
        b = len(word2)
        
        p_w1 = 0
        p_w2 = 0

        result = []
        skip_word1, skip_word2 = False, False
        for i in range(a+b):
            # even case, 0, 2, 4... index is from word1 
            if p_w2 == b:
                # we have reached w2 limit
                skip_word2 = True
            
            if p_w1 == a:
                skip_word1 = True

            # handle case where skip is true
            if skip_word1 and not a == b:
                result.append(word2[p_w2:])
                return "".join(result)

            if skip_word2 and not a == b:
                result.append(word1[p_w1:])
                return "".join(result)

            if i % 2 == 0:
                result.append(word1[p_w1])
                p_w1 += 1
            
            else:
                result.append(word2[p_w2])
                p_w2 += 1
        
        return "".join(result)

            