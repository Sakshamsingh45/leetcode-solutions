class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        score = 0
        i = 0
        s = list(s)
        if x > y:
            a, b = "ab", "ba"
            a_score, b_score = x, y
        else:
            a, b = "ba", "ab"
            a_score, b_score = y, x

        i = 0
        while i < len(s) - 1:
            if s[i] + s[i+1] == a:
                score += a_score
                s.pop(i)
                s.pop(i)
                i = max(i - 2, -1)
            i += 1

        j = 0
        while j < len(s) - 1:
            if s[j] + s[j+1] == b:
                score += b_score
                s.pop(j)
                s.pop(j)
                j = max(j - 2, -1)
            j += 1

        return score
