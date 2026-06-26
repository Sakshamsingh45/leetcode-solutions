class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        freq = {}
        res = []
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
            if freq[n] == 2:
                res.append(n)
        return res
        