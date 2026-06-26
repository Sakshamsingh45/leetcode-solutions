class Solution:
    def palindrom(self, y: int) -> bool:
        y = str(y)
        left, right = 0, len(y) - 1
        while left < right:
            if y[left] != y[right]:
                return False
            left += 1
            right -= 1
        return True

    def converttobase(self, x: int, k: int) -> str:
        res = ""
        while x > 0:
            res = str(x % k) + res
            x = x // k
        return res

    def kMirror(self, k: int, n: int) -> int:
        sum = 0
        count = 0
        b = 1
        while count < n:
            if self.palindrom(b):
                base_k = self.converttobase(b, k)
                if self.palindrom(base_k):
                    sum = sum + b
                    count += 1
            b += 1
        return sum
