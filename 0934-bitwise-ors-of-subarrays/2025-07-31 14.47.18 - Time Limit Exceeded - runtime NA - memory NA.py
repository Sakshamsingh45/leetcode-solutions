class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        a = set()
        for i in range(len(arr)):
            b = arr[i]
            a.add(b)
            for j in range(i + 1, len(arr)):
                b = b | arr[j]
                a.add(b)
        return len(a)
