class Solution:
    def minMaxDifference(self, num: int) -> int:
        s = str(num)

        # Build maximum number: replace first digit ≠ 9 with 9
        for ch in s:
            if ch != '9':
                max_num = int(s.replace(ch, '9'))
                break
        else:
            max_num = int(s)  # already all 9s

        # Build minimum number: replace first digit ≠ 0 with 0
        for ch in s:
            if ch != '0':
                min_num = int(s.replace(ch, '0'))
                break
        else:
            min_num = int(s)  # already all 0s

        return max_num - min_num
