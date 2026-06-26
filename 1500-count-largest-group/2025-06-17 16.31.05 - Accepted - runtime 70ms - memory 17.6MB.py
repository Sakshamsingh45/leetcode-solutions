class Solution:
    def countLargestGroup(self, n: int) -> int:
        digit_sum_count = {}

        for i in range(1, n + 1):
            digit_sum = sum(int(d) for d in str(i))
            if digit_sum in digit_sum_count:
                digit_sum_count[digit_sum] += 1
            else:
                digit_sum_count[digit_sum] = 1
        max_size = max(digit_sum_count.values())
        result = 0
        for count in digit_sum_count.values():
            if count == max_size:
                result += 1

        return result
