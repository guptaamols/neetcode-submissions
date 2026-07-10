class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        num_dict={}
        for num in nums:
            num_dict[num]=1+num_dict.get(num,0)
            if num_dict[num]>=2:
                return True
        
        return False
         