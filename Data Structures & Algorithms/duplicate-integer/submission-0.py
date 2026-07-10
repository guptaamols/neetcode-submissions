class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        from itertools import combinations
        pairs = combinations(nums,2)
        for pair in pairs:
            print(pair[0],pair[1])
            if pair[0]==pair[1]:
                return True
            else:
                pass
        return False