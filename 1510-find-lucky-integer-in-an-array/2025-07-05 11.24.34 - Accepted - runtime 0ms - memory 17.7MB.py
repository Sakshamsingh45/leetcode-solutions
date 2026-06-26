class Solution:
    def findLucky(self, arr: list[int]) -> int:
        max_val = max(arr)  # so we can size frequency array safely
        d = [0] * (max_val + 1)

        for num in arr:
            d[num] += 1

        max_lucky = -1
        for i in range(1, len(d)):
            if d[i] == i:
                max_lucky = i  # not d[i] — we want the number

        return max_lucky
