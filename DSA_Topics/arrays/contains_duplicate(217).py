# leetocode 217. contains duplicates 
# Easy 
class Solution:
    def ContainsDuplicates(self , nums:list[int]) -> bool :
        hashset = set()
        for i in nums :
            if i in hashset : 
                return True 
            hashset.add(i)
        return False 
        
