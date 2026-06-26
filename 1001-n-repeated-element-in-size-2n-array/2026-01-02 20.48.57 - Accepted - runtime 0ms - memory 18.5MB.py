class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        freq={}
        for i in nums:
            if freq.get(i,0)==1:
                return i
            freq[i]=1
            
        