class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        
        for i in range(low, high + 1):
            s = str(i)
            a = len(s)

            if a % 2 == 0:
                b = 0
                c = 0
                
                for k in range(a // 2):
                    b += int(s[k])

                for k in range(a // 2, a):
                    c += int(s[k])
                
                if b == c:
                    count += 1
                    
        return count