class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        if not power:
            return 0

        power.sort()

        # Step 1: group duplicates and store total damage per unique power
        nums = []
        damage = []
        cur = power[0]
        total = power[0]
        for x in power[1:]:
            if x == cur:
                total += x
            else:
                nums.append(cur)
                damage.append(total)
                cur = x
                total = x
        nums.append(cur)
        damage.append(total)

        # Step 2: dynamic programming
        n = len(nums)
        dp = [0] * n
        dp[0] = damage[0]

        for i in range(1, n):
            j = i - 1
            # find last non-conflicting index (nums[j] <= nums[i] - 3)
            while j >= 0 and nums[i] - nums[j] < 3:
                j -= 1
            take = damage[i] + (dp[j] if j >= 0 else 0)
            skip = dp[i - 1]
            dp[i] = max(take, skip)

        return dp[-1]
