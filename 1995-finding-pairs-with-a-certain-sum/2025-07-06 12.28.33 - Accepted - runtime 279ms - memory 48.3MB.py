class FindSumPairs:

    def __init__(self, nums1: list[int], nums2: list[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.freq2 = {}

        # Initialize frequency map for nums2
        for num in nums2:
            self.freq2[num] = self.freq2.get(num, 0) + 1

    def add(self, index: int, val: int) -> None:
        old_val = self.nums2[index]
        new_val = old_val + val

        # Update nums2 value
        self.nums2[index] = new_val

        # Update frequency map
        self.freq2[old_val] -= 1
        if self.freq2[old_val] == 0:
            del self.freq2[old_val]
        self.freq2[new_val] = self.freq2.get(new_val, 0) + 1

    def count(self, tot: int) -> int:
        count = 0
        for a in self.nums1:
            b = tot - a
            count += self.freq2.get(b, 0)
        return count
