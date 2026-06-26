class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        finalsum = 0

        for i in nums:
            if i <= 5:
                continue

            count = 2       
            sum = i + 1

            left = 2
            while left * left <= i:
                if i % left == 0:
                    right = i // left

                    if left == right:
                        count += 1
                        sum += left
                    else:
                        count += 2
                        sum += left + right

                if count > 4:
                    sum = 0
                    break

                left += 1

            if count == 4:
                finalsum += sum

        return finalsum