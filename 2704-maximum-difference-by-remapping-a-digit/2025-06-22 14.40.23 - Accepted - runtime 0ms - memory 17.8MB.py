class Solution:
    def minMaxDifference(self, num: int) -> int:
        mx, mn = 0, float('inf')
        num = list(str(num))
        c = set(num)

        for i in c:
            a, b = 0, 0
            for j in range(len(num)):
                if num[j] == i:
                    a = 10 * a + 9
                    b = 10 * b
                else:
                    a = 10 * a + int(num[j])
                    b = 10 * b + int(num[j])
            mx = max(mx, a)
            mn = min(mn, b)
        
        return mx - mn
