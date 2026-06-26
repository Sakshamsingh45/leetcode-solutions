class Solution:
    def minDistinctFreqPair(self, nums: list[int]) -> list[int]:
        freq={}
        for i in nums:
            freq[i]=freq.get(i,0)+1
        value=sorted(freq.keys())
        for i in range(len(value)):
            for j in range(i+1,len(value)):
                if freq[value[i]]!=freq[value[j]]:
                    return [value[i],value[j]]
        return [-1,-1]