class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq_dict={}
        for num in nums:
            freq_dict[num] = freq_dict.get(num,0) + 1

        buckets = [[] for _ in range(len(nums)+1)]

        for key,value in freq_dict.items():
            buckets[value].append(key)

        res=[]
        for count in range(len(buckets)-1,0,-1):
            for num in buckets[count]:
                res.append(num)
                if len(res) == k:
                    return res