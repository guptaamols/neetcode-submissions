class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashmap = {} # value --> Index

        for ind,num in enumerate(nums):

            diff = target - num

            if diff in hashmap:
                return [hashmap[diff],ind]

            else:
                hashmap[num]=ind