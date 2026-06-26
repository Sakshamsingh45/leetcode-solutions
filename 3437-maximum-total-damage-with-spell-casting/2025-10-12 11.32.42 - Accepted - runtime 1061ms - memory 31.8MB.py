from typing import List

class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        if not power:
            return 0

        # Step 1: sort and group duplicates into (value, total_damage_for_value)
        power.sort()
        nums = []     # unique values
        damage = []   # total damage for each unique value
        cur = power[0]
        tot = power[0]
        for x in power[1:]:
            if x == cur:
                tot += x
            else:
                nums.append(cur)
                damage.append(tot)
                cur = x
                tot = x
        nums.append(cur)
        damage.append(tot)

        # Step 2: DP where dp[i] = best damage using nums[0..i]
        n = len(nums)
        dp = [0] * n
        dp[0] = damage[0]

        # helper: find rightmost index j < i such that nums[j] <= nums[i] - 3
        def find_last_non_conflicting(nums, i):
            target = nums[i] - 3
            lo, hi = 0, i - 1
            ans = -1
            while lo <= hi:
                mid = (lo + hi) // 2
                if nums[mid] <= target:
                    ans = mid
                    lo = mid + 1
                else:
                    hi = mid - 1
            return ans

        for i in range(1, n):
            j = find_last_non_conflicting(nums, i)
            take = damage[i] + (dp[j] if j != -1 else 0)
            skip = dp[i - 1]
            dp[i] = max(take, skip)

        return dp[-1]
