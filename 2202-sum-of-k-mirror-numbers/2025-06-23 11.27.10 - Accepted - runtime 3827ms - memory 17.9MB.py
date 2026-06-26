class Solution:
    def palindrom(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    def converttobase(self, x: int, k: int) -> str:
        res = ""
        while x > 0:
            res = str(x % k) + res
            x //= k
        return res

    def kMirror(self, k: int, n: int) -> int:
        def generate_palindromes(length):
            # Generate palindromes of a given length
            half_len = (length + 1) // 2
            start = 10**(half_len - 1)
            end = 10**half_len
            for i in range(start, end):
                s = str(i)
                if length % 2 == 0:
                    yield int(s + s[::-1])
                else:
                    yield int(s + s[-2::-1])

        count = 0
        total = 0
        length = 1

        while count < n:
            for p in generate_palindromes(length):
                if self.palindrom(self.converttobase(p, k)):
                    total += p
                    count += 1
                    if count == n:
                        return total
            length += 1

        return total
