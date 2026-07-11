class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for shift in range(1,len(nums)):
            shifted = nums[shift:]+nums[0:shift]
            
            for i in range(len(nums)):
                if nums[i] + shifted[i] == target:
                    indices = [i,(i + shift) % len(nums)]
                    indices.sort()
                    return indices