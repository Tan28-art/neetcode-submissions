from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hashmap = {}
        
        for i in nums:
            if (i not in hashmap):
                hashmap.update({i:1})

            else:
                hashmap[i] += 1

        list_values = list(hashmap.values())
        #print(list_values)
        list_values.sort(reverse = True)
        
        final_freq_list = []
        for i in range(k):
            final_freq_list.append(list_values[i])
            
        solution = []
        for k, v in hashmap.items():
            if v in final_freq_list and k not in solution:
                solution.append(k)
                #final_freq_list.remove(v)
                    
        #print(solution)
        return solution