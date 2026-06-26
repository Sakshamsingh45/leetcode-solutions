class Solution:
    def findLHS(self, nums):
        # Step 1: Build frequency map manually
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        # Step 2: Find max length where key and key+1 both exist
        max_len = 0
        for num in freq:
            if num + 1 in freq:
                length = freq[num] + freq[num + 1]
                if length > max_len:
                    max_len = length

        return max_len
