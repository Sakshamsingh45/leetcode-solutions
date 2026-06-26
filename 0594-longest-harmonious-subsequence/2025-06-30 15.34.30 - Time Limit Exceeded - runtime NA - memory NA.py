class Solution:
    def findLHS(self, nums):
        nums_list = list(set(nums))  # Convert set to list for indexing
        max_len = 0

        for i in range(len(nums_list)):
            for j in range(i + 1, len(nums_list)):
                if abs(nums_list[i] - nums_list[j]) == 1:
                    total = nums.count(nums_list[i]) + nums.count(nums_list[j])
                    if total > max_len:
                        max_len = total

        return max_len
