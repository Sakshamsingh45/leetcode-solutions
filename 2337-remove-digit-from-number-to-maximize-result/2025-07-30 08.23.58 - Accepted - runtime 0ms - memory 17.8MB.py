class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        max_num = ""
        for i in range(len(number)):
            if number[i] == digit:
                candidate = number[:i] + number[i+1:]
                if candidate > max_num:
                    max_num = candidate
        return max_num
