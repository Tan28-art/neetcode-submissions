class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) <= 1:
            return "" if len(strs) == 0 else strs[0]
        
        n = len(strs)
        
        min_s = strs[0]
        l = len(min_s)
        for s in strs:
            if len(s) < l:
                min_s = s
                l = len(s)

        prefix = ""
        for i in range(l):
            for s in strs:
                if s[i] != strs[0][i]:
                    return prefix
            prefix += strs[0][i]

        return prefix
