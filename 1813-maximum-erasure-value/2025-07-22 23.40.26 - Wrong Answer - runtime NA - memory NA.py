class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        score = 0
        a=[]
        for i in range(len(nums)):
            if not a or nums[i] not in a:
                a.append(nums[i])
                score+=nums[i]
        return score
        