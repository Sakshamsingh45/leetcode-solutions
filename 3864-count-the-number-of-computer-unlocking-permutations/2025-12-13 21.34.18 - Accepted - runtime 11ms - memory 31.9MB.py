class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        count=1
        MOD=10**9+7
        for i in range(1,len(complexity)):
            if complexity[i]<=complexity[0]:
                return 0
        for j in range(1,len(complexity)):
            count=count*j%MOD
        return count
