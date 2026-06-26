class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MOD=10**9+7
        ans=""
        for i in range(n+1):
            ans+=bin(i)[2:]
        return int(ans,2)%MOD